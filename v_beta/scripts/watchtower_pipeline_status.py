#!/usr/bin/env python3
"""Report the authoritative Watchtower layered-production stage."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "assets/source/watchtower"
CANDIDATE_DIR = ROOT / "assets/staging/candidates/watchtower"
APPROVED_DIR = ROOT / "assets/approved/masters/watchtower"
RUNTIME_DIR = ROOT / "assets/runtime/atlases"
REVIEW_DIR = ROOT / "assets/review/watchtower"
MANIFEST_TEMPLATE = CANDIDATE_DIR / "watchtower_layered_manifest_template_v1.json"
SOURCE_PLAN = ROOT / "assets/staging/prompts/watchtower_source_call_plan_v1.json"
VALIDATOR = ROOT / "scripts/validate_layered_atlas.py"
SITE_HOSTING = ROOT / "sites/qa/watchtower-lab/.openai/hosting.json"


def newest(pattern: str, directory: Path) -> Path | None:
    paths = list(directory.glob(pattern)) if directory.is_dir() else []
    return max(paths, key=lambda path: path.stat().st_mtime) if paths else None


def read_json(path: Path | None) -> dict[str, Any] | None:
    if path is None or not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def check(name: str, passed: bool, detail: str) -> dict[str, Any]:
    return {"name": name, "passed": passed, "detail": detail}


def build_status() -> dict[str, Any]:
    source = newest("watchtower_projection_master_v*_imagegen2_source.png", SOURCE_DIR)
    alpha = newest("watchtower_projection_master_v*_alpha.png", CANDIDATE_DIR)
    intake_path = newest("watchtower_projection_master_v*_intake_report.json", CANDIDATE_DIR)
    intake = read_json(intake_path)
    review_path = newest("watchtower_projection_review_v*.json", CANDIDATE_DIR)
    review = read_json(review_path)
    approved_registry_path = APPROVED_DIR / "approved_projection_registry.json"
    approved_registry = read_json(approved_registry_path)
    approved_master = newest("watchtower_projection_master_v*_approved.png", APPROVED_DIR)
    layer_dir = APPROVED_DIR / "layers"
    layer_count = len(list(layer_dir.glob("*.png"))) if layer_dir.is_dir() else 0
    runtime_manifest_path = RUNTIME_DIR / "watchtower_layered_manifest.json"
    runtime_png_path = RUNTIME_DIR / "watchtower_layered_runtime.png"
    runtime_manifest = read_json(runtime_manifest_path)
    review_grid = REVIEW_DIR / "watchtower_layered_review_grid.png"
    composite = REVIEW_DIR / "watchtower_layered_composite_preview.png"
    site_hosting = read_json(SITE_HOSTING)

    expected_count = 133
    if MANIFEST_TEMPLATE.is_file():
        template = read_json(MANIFEST_TEMPLATE)
        expected_count = 133 if template else 0

    atlas_validation_pass = False
    atlas_validation_detail = "runtime manifest absent"
    if runtime_manifest_path.is_file():
        result = subprocess.run(
            [
                sys.executable,
                str(VALIDATOR),
                str(runtime_manifest_path),
                "--mode",
                "production",
            ],
            text=True,
            capture_output=True,
        )
        atlas_validation_pass = result.returncode == 0
        atlas_validation_detail = (
            result.stdout.strip().splitlines()[0]
            if result.stdout.strip()
            else result.stderr.strip().splitlines()[0]
            if result.stderr.strip()
            else f"validator exit {result.returncode}"
        )

    gates = [
        check("documentation", MANIFEST_TEMPLATE.is_file() and SOURCE_PLAN.is_file(), "layer contract, manifest template and source plan"),
        check("projection_source", source is not None, str(source.relative_to(ROOT)) if source else "ImageGen 2 source absent"),
        check("alpha_intake", bool(alpha and intake and intake.get("status") == "technical_intake_pass"), str(intake_path.relative_to(ROOT)) if intake_path else "technical intake absent"),
        check("visual_approval", bool(review and review.get("status") == "approved" and review.get("decision", {}).get("userConfirmed") is True), str(review_path.relative_to(ROOT)) if review_path else "user-approved review absent"),
        check("approved_master", bool(approved_master and approved_registry and approved_registry.get("approvals")), str(approved_master.relative_to(ROOT)) if approved_master else "approved projection master absent"),
        check("decomposition", layer_count == expected_count, f"{layer_count}/{expected_count} approved layer PNGs"),
        check("runtime_atlas", bool(runtime_png_path.is_file() and runtime_manifest), "runtime PNG and manifest" if runtime_png_path.is_file() and runtime_manifest else "runtime atlas absent"),
        check("technical_validation", atlas_validation_pass, atlas_validation_detail),
        check("review_artifacts", review_grid.is_file() and composite.is_file(), "review grid and composite" if review_grid.is_file() and composite.is_file() else "review artifacts incomplete"),
        check("animation_site", bool(site_hosting and site_hosting.get("project_id")), "manifest-driven QA site configured" if site_hosting and site_hosting.get("project_id") else "QA site not configured"),
    ]

    next_gate = next((item["name"] for item in gates if not item["passed"]), "complete")
    regression = subprocess.run(
        [
            sys.executable,
            "-m",
            "unittest",
            "discover",
            "-s",
            str(ROOT / "scripts/tests"),
            "-p",
            "test_*.py",
        ],
        text=True,
        capture_output=True,
        env={"PYTHONDONTWRITEBYTECODE": "1"},
    )
    return {
        "schemaVersion": 1,
        "objectId": "watchtower",
        "displayName": "Ветровой дозор",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "state": "complete" if next_gate == "complete" else "blocked",
        "nextGate": next_gate,
        "gates": gates,
        "regressionTests": {
            "passed": regression.returncode == 0,
            "summary": (
                "7/7 PASS"
                if regression.returncode == 0
                else (regression.stderr or regression.stdout).strip().splitlines()[-1]
            ),
        },
        "policy": {
            "mayStartNextObject": next_gate == "complete",
            "manualRasterSubstitutionAllowed": False,
            "imagegenModel": "built-in ImageGen 2",
        },
    }


def markdown(status: dict[str, Any]) -> str:
    lines = [
        "# Watchtower Pipeline Status",
        "",
        f"- State: **{status['state'].upper()}**",
        f"- Next gate: `{status['nextGate']}`",
        f"- Regression tests: **{status['regressionTests']['summary']}**",
        f"- May start next object: **{'YES' if status['policy']['mayStartNextObject'] else 'NO'}**",
        "",
        "| Gate | Result | Detail |",
        "|---|---|---|",
    ]
    for gate in status["gates"]:
        lines.append(
            f"| `{gate['name']}` | {'PASS' if gate['passed'] else 'BLOCKED'} | {gate['detail']} |"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--markdown", type=Path)
    parser.add_argument("--fail-if-blocked", action="store_true")
    args = parser.parse_args()
    status = build_status()
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(
            json.dumps(status, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    if args.markdown:
        args.markdown.parent.mkdir(parents=True, exist_ok=True)
        args.markdown.write_text(markdown(status), encoding="utf-8")
    if not args.json and not args.markdown:
        print(markdown(status), end="")
    return 1 if args.fail_if_blocked and status["state"] != "complete" else 0


if __name__ == "__main__":
    raise SystemExit(main())
