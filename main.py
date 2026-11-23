#!/usr/bin/env python3
"""Office Jokes — make.fun bounty entry.

Writes one original one-line joke about office life to
$MAKEFUN_OUTPUT_DIR/entry.txt (default ./out).

Deterministic: no network, no randomness, no secrets, no input files.
The joke is a constant in this file, so every run produces byte-identical
output.
"""
import os
from pathlib import Path

JOKE = (
    "My out-of-office reply answers emails faster than I do, "
    "so HR promoted it and put me on a performance plan."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
