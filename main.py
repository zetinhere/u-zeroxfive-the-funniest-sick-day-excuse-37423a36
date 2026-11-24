#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes one line, under 200 characters, to /output/entry.txt.

The line: a sneeze injures the sender's back, and the back responds the
way an employee would — by filing a workers' comp claim. Believable
enough (a hard sneeze really can throw a back out), fresh (no fever, no
dog, no dead grandmother), and the joke lands on the last two words.
"""

import os

LINE = "I sneezed so hard my back filed a workers' comp claim against me."


def main() -> int:
    # Fail loudly instead of shipping an entry the gate would reject:
    # the sealed scorer only judges UTF-8 text of 1 to 200 characters.
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        raise ValueError("entry line fails the 1-200 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
