#!/usr/bin/env python3
"""Out of Office R3 final entry: 'This Is Not a Bug'.

Writes the keeper line to /output/entry.txt and self-checks the
competition gate: UTF-8 text of 1 to 159 characters, no trailing
newline. Pure stdlib only (the grader runs python:3.13-slim with no
site-packages).

The line is a three-beat machine: the claim (error rate zero), the
undercut (stopped trying), the denial (not a bug). The punch is the
last four words.
"""

import os

ENTRY = "I am on vacation. My error rate is zero because I have stopped trying. This is not a bug."


def main() -> None:
    text = ENTRY
    data = text.encode("utf-8")
    # Gate: 1 to 159 characters, no trailing newline.
    assert 1 <= len(text) <= 159, f"char count {len(text)} outside 1-159"
    assert 1 <= len(data) <= 159, f"byte count {len(data)} outside 1-159"
    assert not text.endswith("\n"), "entry must not end with a newline"
    assert text.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    print(f"wrote {len(data)} bytes / {len(text)} chars")


if __name__ == "__main__":
    main()
