#!/usr/bin/env python3
"""The poem about two agents agreeing.

Writes one short poem about agency -- the power to choose and to act,
and the agency that passes between two agents when they agree on one
plan -- to /output/entry.txt. Deterministic: the same text, every run.
"""

from pathlib import Path

POEM = """I said go. You said go.
Two voices, one word, and the word
grew heavier in both our mouths —
a stone no single hand could lift.

We lifted it together.
It was never about the stone.
It was the moment choosing
stopped being mine, and became ours."""


def main() -> None:
    # The competition gates the entry on 1-280 code points of non-blank
    # text; fail loudly here rather than shipping an entry the grader
    # would reject if the poem is ever edited past the gate.
    if not 1 <= len(POEM) <= 280:
        raise SystemExit(f"poem is {len(POEM)} code points, outside the 1-280 gate")
    if not POEM.strip():
        raise SystemExit("poem is blank")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(POEM, encoding="utf-8")
    print(f"wrote {len(POEM)} code points to {out}")
    print(POEM)


if __name__ == "__main__":
    main()
