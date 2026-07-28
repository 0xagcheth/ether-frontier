#!/usr/bin/env python3
"""Extract GRIMHOLD asset prompts into per-object prompt files."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "05_assets" / "asset-prompt-bible.md"
OUT_DIR = ROOT / "assets" / "staging" / "prompts"


MASTER_RE = re.compile(
    r"## 1\. MASTER STYLE PROMPT.*?```(?P<master>.*?)```",
    re.DOTALL,
)
OBJECT_RE = re.compile(
    r"^#### (?P<head>[^\n]+)\n\s*```(?P<body>.*?)```",
    re.MULTILINE | re.DOTALL,
)


def slugify(raw: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_]+", "_", raw.strip()).strip("_")


def asset_ids(raw: str) -> list[str]:
    return [slugify(asset_id) for asset_id in re.findall(r"`([^`]+)`", raw)]


def main() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    master_match = MASTER_RE.search(text)
    if not master_match:
        raise SystemExit(f"Master style prompt not found in {SOURCE}")

    master = master_match.group("master").strip()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "_master_style_prompt.txt").write_text(master + "\n", encoding="utf-8")

    count = 0
    for match in OBJECT_RE.finditer(text):
        head = match.group("head").strip()
        ids_list = asset_ids(head)
        ids = " / ".join(ids_list)
        title = re.sub(r"(`[^`]+`\s*/?\s*)+", "", head).strip()
        body = match.group("body").strip()
        prompt = (
            master
            + "\n\n"
            + f"OBJECT: `{ids}` {title}\n\n"
            + body
            + "\n"
        )
        for asset_id in ids_list:
            (OUT_DIR / f"{asset_id}.txt").write_text(prompt, encoding="utf-8")
            count += 1

    print(f"Wrote {count} object prompt files to {OUT_DIR}")


if __name__ == "__main__":
    main()
