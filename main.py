#!/usr/bin/env python3
"""Terabytes by Carrier Pigeon.

Writes one sentence (at most 200 characters) pitching a bizarre startup
idea that sounds absurd until the business logic lands: physically
delivering huge files by carrier pigeon beats a slow upload, so film
studios pay per gigabyte flown.

Run: python3 main.py
Writes: $MAKEFUN_OUTPUT_DIR/entry.txt (default: ./output/entry.txt)
"""

import os

PITCH = ("We deliver terabytes by carrier pigeon: a USB strapped to a bird "
         "crosses town faster than your upload, and the bird never buffers, "
         "so studios pay per gigabyte flown.")

MAX_CHARS = 200


def check_line(line):
    """Gate the pitch the same way the sealed scorer does."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    text = line.strip()
    if not text:
        raise ValueError("entry is empty")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d characters, over the 200 limit"
                         % len(text))
    return text


def emit(text):
    """Write the pitch to $MAKEFUN_OUTPUT_DIR/entry.txt, nothing else."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return path


def verify_written(path, text):
    """Read the written file back and make sure it matches byte for byte."""
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise ValueError("written entry does not match the pitch")
    if len(written.encode("utf-8")) != len(text):
        raise ValueError("written entry is not plain single-byte text")
    return written


def main():
    line = check_line(PITCH)
    path = emit(line)
    verify_written(path, line)
    print("Wrote %s (%d characters)" % (path, len(line)))


if __name__ == "__main__":
    main()
