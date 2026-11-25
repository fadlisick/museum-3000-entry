#!/usr/bin/env python3
"""Museum of the Year 3000 - museum label entry.

Writes one deadpan museum label to /output/entry.txt: the year-3000
curator's label beside a lint roller from today.
"""

import os
import stat
import sys

ENTRY = (
    "Lint roller, c. 2023. A ceremonial adhesive wand, rolled over "
    "clothing to remove the sins of pet ownership."
)

GATE_MIN = 1
GATE_MAX = 200


def output_path():
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def gate_ok(text):
    if not (GATE_MIN <= len(text) <= GATE_MAX):
        return False
    if text != text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if "\u2014" in text:
        return False
    return True


def write_entry():
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    return path


def verify(path):
    with open(path, "rb") as handle:
        raw = handle.read()
    if raw != ENTRY.encode("utf-8"):
        raise SystemExit("entry.txt bytes do not match the locked label")
    with open(path, "r", encoding="utf-8", newline="") as handle:
        seen = handle.read()
    if seen != ENTRY:
        raise SystemExit("entry.txt does not match the locked label")
    if not gate_ok(seen):
        raise SystemExit("entry.txt fails the gate self-check")
    return len(seen)


def main():
    path = write_entry()
    size = verify(path)
    print(f"wrote {path} ({size} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
