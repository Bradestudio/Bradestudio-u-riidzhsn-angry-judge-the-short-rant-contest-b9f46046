"""Angry Judge: The Short Rant Contest — make.fun entry.

Writes the rant to entry.txt in MAKEFUN_OUTPUT_DIR
(fallback /output). Deterministic, stdlib only, no network, no clock.
"""

import os

ENTRY = (
    "I did not steal the rice. I scanned it, paid for it, bagged it \u2014 "
    "and still the self-checkout screams 'unexpected item in the bagging "
    "area', like I smuggled it under my shirt. It has one job: watch me "
    "pay. Instead it freezes, summons a human, and leaves me holding my "
    "own groceries like a suspect while the queue holds my trial. The "
    "machine trusts no one, least of all the customer it just charged."
)


def main():
    line = ENTRY
    if not line or line != line.strip():
        raise SystemExit("entry must be non-blank with no leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(line) <= 400:
        raise SystemExit("entry must be 1-400 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(path, "rb") as f:
        written = f.read()
    if written != line.encode("utf-8"):
        raise SystemExit("written entry.txt does not match the gated line")


if __name__ == "__main__":
    main()
