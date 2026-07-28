#!/usr/bin/env python3
"""Validate an ImageGen source-call plan before asset generation."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def validate(plan: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    calls = plan.get("calls")
    if not isinstance(calls, list) or not calls:
        return ["calls must be a non-empty list"]

    ids = [call.get("id") for call in calls]
    if any(not isinstance(call_id, str) or not call_id for call_id in ids):
        errors.append("every call requires a non-empty id")
    if len(ids) != len(set(ids)):
        errors.append("call ids must be unique")
    known = set(ids)
    available = {"human_projection_approval"}
    seen: set[str] = set()
    output_names: set[str] = set()

    for index, call in enumerate(calls, start=1):
        call_id = call.get("id", f"call[{index}]")
        for field in (
            "unit",
            "dependsOn",
            "referencePolicy",
            "expectedOutput",
            "promptSuffix",
        ):
            if field not in call:
                errors.append(f"{call_id}: missing {field}")
        dependencies = call.get("dependsOn", [])
        if not isinstance(dependencies, list):
            errors.append(f"{call_id}: dependsOn must be a list")
            continue
        for dependency in dependencies:
            if dependency not in known and dependency not in available:
                errors.append(f"{call_id}: unknown dependency {dependency}")
            if dependency in known and dependency not in seen:
                errors.append(f"{call_id}: dependency {dependency} appears later")
        output = call.get("expectedOutput")
        if output in output_names:
            errors.append(f"{call_id}: duplicate expectedOutput {output}")
        output_names.add(output)
        suffix = str(call.get("promptSuffix", "")).lower()
        forbidden = ("labelled grid", "all layers on one", "runtime atlas sheet")
        if any(term in suffix for term in forbidden):
            errors.append(f"{call_id}: prompt requests forbidden combined sheet")
        seen.add(call_id)

    if calls[0].get("unit") != "assembled_projection_master":
        errors.append("first call must be assembled_projection_master")
    gate = plan.get("gates", {})
    if gate.get("projectionMasterApprovalRequiredBeforeCall") != 2:
        errors.append("projection approval gate must start before call 2")
    if gate.get("oneUnitPerCall") is not True:
        errors.append("oneUnitPerCall must be true")
    if gate.get("atlasSheetForbidden") is not True:
        errors.append("atlasSheetForbidden must be true")
    if plan.get("generationModel") != "built-in ImageGen 2":
        errors.append("generationModel must be built-in ImageGen 2")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("plan", type=Path)
    args = parser.parse_args()
    try:
        plan = json.loads(args.plan.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 2
    errors = validate(plan)
    if errors:
        print(f"FAIL ({len(errors)} errors)")
        for message in errors:
            print(f"- {message}")
        return 1
    print(f"PASS: {len(plan['calls'])} ordered ImageGen 2 source calls")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
