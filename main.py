#!/usr/bin/env python3
"""Two Days of Quiet Dread - one-line code review comment.

Writes a single line to /output/entry.txt: it approves the pull request
in a flat, tired-engineer voice, and the dread sits quietly in the
second half instead of being shouted. One line, at most 140 chars.
"""

import os

COMMENT = "Approved. It passes. One day this will be legacy code, and so will we."


def main():
    text = COMMENT.strip()
    if "\n" in text or "\r" in text:
        raise ValueError("comment must be a single line")
    if not 1 <= len(text) <= 140:
        raise ValueError(f"comment is {len(text)} characters, must be 1-140")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
