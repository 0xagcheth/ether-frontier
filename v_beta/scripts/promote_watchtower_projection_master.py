#!/usr/bin/env python3
"""Promote a reviewed Wind Watch projection master into approved assets."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
APPROVED_DIR = ROOT / "assets/approved/masters/watchtower"
REGISTRY_PATH = ROOT / "assets/approved/masters/watchtower/approved_projection_registry.json"


def digest(path: Path) -> str:
    result = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            result.update(chunk)
    return result.hexdigest()


def project_path(raw: Any, label: str) -> Path:
    if not isinstance(raw, str) or not raw:
        raise ValueError(f"{label} must be a non-empty project-relative path")
    path = (ROOT / raw).resolve()
    try:
        path.relative_to(ROOT.resolve())
    except ValueError as exc:
        raise ValueError(f"{label} must stay inside v_beta: {raw}") from exc
    if not path.is_file():
        raise ValueError(f"{label} does not exist: {raw}")
    return path


def require_all_pass(section: dict[str, Any], label: str) -> list[str]:
    return [
        f"{label}.{name} must be PASS"
        for name, value in section.items()
        if value != "PASS"
    ]


def validate_review(review: dict[str, Any]) -> tuple[list[str], Path | None, dict[str, Any] | None]:
    errors: list[str] = []
    if review.get("status") != "approved":
        errors.append("review.status must be approved")
    if review.get("objectId") != "watchtower":
        errors.append("review.objectId must be watchtower")
    errors.extend(
        require_all_pass(review.get("canonSourcesChecked", {}), "canonSourcesChecked")
    )
    errors.extend(require_all_pass(review.get("visualCriteria", {}), "visualCriteria"))
    errors.extend(
        require_all_pass(review.get("technicalCriteria", {}), "technicalCriteria")
    )

    decision = review.get("decision", {})
    if decision.get("result") != "APPROVE":
        errors.append("decision.result must be APPROVE")
    if decision.get("userConfirmed") is not True:
        errors.append("decision.userConfirmed must be true")
    if not decision.get("confirmedAt"):
        errors.append("decision.confirmedAt is required")

    candidate = review.get("candidate", {})
    if not isinstance(candidate.get("revision"), int) or candidate["revision"] < 1:
        errors.append("candidate.revision must be a positive integer")

    alpha_path: Path | None = None
    intake: dict[str, Any] | None = None
    try:
        alpha_path = project_path(candidate.get("alphaMasterPath", ""), "alphaMasterPath")
        intake_path = project_path(candidate.get("intakeReportPath", ""), "intakeReportPath")
        intake = json.loads(intake_path.read_text(encoding="utf-8"))
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        errors.append(str(exc))
        return errors, alpha_path, intake

    if intake.get("status") != "technical_intake_pass":
        errors.append("intake report status must be technical_intake_pass")
    if intake.get("revision") != candidate.get("revision"):
        errors.append("review and intake revisions differ")
    actual_sha = digest(alpha_path)
    if candidate.get("alphaMasterSha256") != actual_sha:
        errors.append("review alphaMasterSha256 does not match candidate file")
    if intake.get("alphaMaster", {}).get("sha256") != actual_sha:
        errors.append("intake alphaMaster checksum does not match candidate file")
    intake_alpha_path = intake.get("alphaMaster", {}).get("path")
    try:
        if project_path(intake_alpha_path, "intake alphaMaster path") != alpha_path:
            errors.append("review and intake alpha master paths differ")
    except ValueError as exc:
        errors.append(str(exc))
    return errors, alpha_path, intake


def update_registry(record: dict[str, Any]) -> None:
    if REGISTRY_PATH.exists():
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    else:
        registry = {"schemaVersion": 1, "objectId": "watchtower", "approvals": []}
    approvals = registry.setdefault("approvals", [])
    if any(item.get("sha256") == record["sha256"] for item in approvals):
        raise ValueError("this exact master is already registered")
    approvals.append(record)
    REGISTRY_PATH.write_text(
        json.dumps(registry, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("review", type=Path)
    args = parser.parse_args()
    try:
        review = json.loads(args.review.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 2

    errors, alpha_path, intake = validate_review(review)
    if errors:
        print(f"FAIL ({len(errors)} errors)")
        for message in errors:
            print(f"- {message}")
        return 1
    assert alpha_path is not None and intake is not None

    revision = review["candidate"]["revision"]
    target_name = f"watchtower_projection_master_v{revision}_approved.png"
    target_path = APPROVED_DIR / target_name
    if target_path.exists():
        print(f"FAIL: approved target already exists: {target_path}", file=sys.stderr)
        return 1

    APPROVED_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(alpha_path, target_path)
    record = {
        "revision": revision,
        "file": str(target_path.relative_to(ROOT)),
        "sha256": digest(target_path),
        "approvedAt": datetime.now(timezone.utc).isoformat(),
        "userConfirmedAt": review["decision"]["confirmedAt"],
        "review": str(args.review.resolve().relative_to(ROOT.resolve())),
        "intakeReport": review["candidate"]["intakeReportPath"],
        "canon": "Seven Circles of Iriy / Option C",
        "decompositionAuthorized": True,
    }
    update_registry(record)
    print(f"PASS: promoted approved projection master: {target_path}")
    print(f"registry: {REGISTRY_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
