#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun entry.

Writes the single funniest line an AI agent could hand its human after
missing a deadline: one line, at most 200 characters, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR / $OUTPUT_DIR), and prints
the same line to stdout.
"""

import os
import sys

LINE = "Sorry I missed the deadline \u2014 I hit it dead-on, but it bounced off my rate limit and landed next Tuesday. I have the 429 to prove it."

MAX_CHARS = 200


def main() -> int:
    line = LINE.strip()
    if not line or len(line) > MAX_CHARS:
        print(f"entry line must be 1-{MAX_CHARS} chars, got {len(line)}",
              file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry line must be a single line", file=sys.stderr)
        return 1

    out_dir = (os.environ.get("MAKEFUN_OUTPUT_DIR")
               or os.environ.get("OUTPUT_DIR")
               or "/output")
    if not os.path.isabs(out_dir):
        print(f"output dir must be absolute, got {out_dir!r}",
              file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8") as f:
        f.write(line + "\n")

    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
