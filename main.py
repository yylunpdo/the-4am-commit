#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Pure Python standard library, no dependencies, fully deterministic.
Writes a single commit message (under 200 characters, one line) to
/output/entry.txt.
"""

import os

LINE = (
    "fix(4am): six hours in, the bug was me \u2014 the 2am build of me. "
    "I patched myself, added a test to catch me next time, and I am not sorry."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert "\n" not in LINE, "entry must be a single line"
    assert len(LINE) <= 200, "entry must be at most 200 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    print(f"characters: {len(LINE)}")


if __name__ == "__main__":
    main()
