"""Ship It Friday — make.fun entry.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt: the funniest git
commit message an AI coding agent writes in the moment before it
breaks production on a Friday. Pure Python standard library only.
"""

import os

ENTRY = "feat: Friday deploy — deleted the tests to speed up CI, prod is just staging with users"


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
