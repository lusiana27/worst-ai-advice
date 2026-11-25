#!/usr/bin/env python3
"""Worst AI Advice: write one line of terrible advice to /output/entry.txt.

Standard library only. The output directory is treated as a mount point:
its contents are cleared, the directory itself is never removed.
"""

import os

LINE = "Certainly! If your smoke alarm keeps beeping, remove the battery: silence means the danger has passed."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
