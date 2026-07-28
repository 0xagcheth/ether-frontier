#!/usr/bin/env python3
"""Intake an ImageGen 2 Wind Watch source and prepare its alpha master."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CHROMA_TOOL = (
    Path.home()
    / ".codex/skills/.system/imagegen/scripts/remove_chroma_key.py"
)
SOURCE_DIR = ROOT / "assets/source/watchtower"
CANDIDATE_DIR = ROOT / "assets/staging/candidates/watchtower"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def alpha_stats(path: Path) -> dict[str, Any]:
    with Image.open(path) as image:
        rgba = image.convert("RGBA")
        width, height = rgba.size
        alpha = rgba.getchannel("A")
        bbox = alpha.getbbox()
        histogram = alpha.histogram()
    total = width * height
    transparent = histogram[0]
    partial = sum(histogram[1:255])
    opaque = histogram[255]
    if bbox is None:
        raise ValueError("alpha master is fully transparent")
    left, top, right, bottom = bbox
    margins = {
        "left": left,
        "top": top,
        "right": width - right,
        "bottom": height - bottom,
    }
    return {
        "width": width,
        "height": height,
        "alphaBBox": [left, top, right, bottom],
        "marginsPx": margins,
        "transparentPixels": transparent,
        "partialPixels": partial,
        "opaquePixels": opaque,
        "transparentRatio": round(transparent / total, 6),
        "partialRatio": round(partial / total, 6),
        "minimumMarginPx": min(margins.values()),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--revision", type=int, required=True)
    parser.add_argument("--minimum-margin", type=int, default=24)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    if not args.input.is_file():
        print(f"FAIL: input does not exist: {args.input}", file=sys.stderr)
        return 1
    if args.revision < 1:
        print("FAIL: revision must be positive", file=sys.stderr)
        return 1
    if not CHROMA_TOOL.is_file():
        print(f"FAIL: canonical chroma tool missing: {CHROMA_TOOL}", file=sys.stderr)
        return 1

    source_name = f"watchtower_projection_master_v{args.revision}_imagegen2_source.png"
    alpha_name = f"watchtower_projection_master_v{args.revision}_alpha.png"
    report_name = f"watchtower_projection_master_v{args.revision}_intake_report.json"
    source_path = SOURCE_DIR / source_name
    alpha_path = CANDIDATE_DIR / alpha_name
    report_path = CANDIDATE_DIR / report_name

    targets = (source_path, alpha_path, report_path)
    existing = [path for path in targets if path.exists()]
    if existing and not args.force:
        print(
            "FAIL: outputs already exist; use a new revision or --force: "
            + ", ".join(str(path) for path in existing),
            file=sys.stderr,
        )
        return 1

    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    CANDIDATE_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(args.input, source_path)

    command = [
        sys.executable,
        str(CHROMA_TOOL),
        "--input",
        str(source_path),
        "--out",
        str(alpha_path),
        "--auto-key",
        "border",
        "--soft-matte",
        "--transparent-threshold",
        "12",
        "--opaque-threshold",
        "88",
        "--spill-cleanup",
    ]
    if args.force:
        command.append("--force")
    result = subprocess.run(command, text=True, capture_output=True)
    if result.returncode:
        print(result.stdout, end="")
        print(result.stderr, end="", file=sys.stderr)
        return result.returncode

    stats = alpha_stats(alpha_path)
    technical_checks = {
        "sourcePreserved": source_path.is_file(),
        "alphaExists": alpha_path.is_file(),
        "hasTransparentBackground": stats["transparentPixels"] > 0,
        "hasVisibleContent": stats["opaquePixels"] + stats["partialPixels"] > 0,
        "noClippingByMargin": stats["minimumMarginPx"] >= args.minimum_margin,
        "sourceAndAlphaCanvasMatch": False,
    }
    with Image.open(source_path) as source, Image.open(alpha_path) as alpha:
        technical_checks["sourceAndAlphaCanvasMatch"] = source.size == alpha.size

    report = {
        "status": (
            "technical_intake_pass"
            if all(technical_checks.values())
            else "technical_intake_fail"
        ),
        "objectId": "watchtower",
        "displayName": "Ветровой дозор",
        "revision": args.revision,
        "source": {
            "path": str(source_path.relative_to(ROOT)),
            "sha256": sha256(source_path),
        },
        "alphaMaster": {
            "path": str(alpha_path.relative_to(ROOT)),
            "sha256": sha256(alpha_path),
            **stats,
        },
        "technicalChecks": technical_checks,
        "manualVisualGate": {
            "approved": False,
            "required": [
                "true top-down orthographic 90 degrees",
                "premium separate solid-cardboard pieces",
                "exactly 20 parapet stones",
                "exactly 2 opposite access notches",
                "8 radial deck sectors",
                "balanced lightweight crossbow, not Ballista",
                "4 copper bearing arcs",
                "4 reserve bolts plus 1 empty slot",
                "no legacy symbols or clipping",
            ],
        },
        "chromaToolOutput": result.stdout.strip().splitlines(),
    }
    report_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"{report['status']}: {alpha_path}")
    print(f"report: {report_path}")
    return 0 if report["status"] == "technical_intake_pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
