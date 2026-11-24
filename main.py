#!/usr/bin/env python3
"""Write one robot wedding vow to /output/entry.txt.

The vow (v2 — revised from v1): a robot promises to love past its
warranty and through every update, because even when a newer model
is built, its heart will still boot for its partner. One sentence,
135 characters.

Why v2 beats v1: v1 ("stay compatible ... no patch will ever make me
love you less") was sweet but its laugh was thin — compatibility is a
flat setup and the payoff only restates the promise. v2 gets its laugh
from the situation itself: the robot knows it will be obsolete one day
(a newer model is coming) and vows anyway, which is both the joke and
the tenderness. The machine voice is denser and more specific
(warranty, update, newer model, boot), and the payoff — "my heart will
still boot for you" — is a line only a machine could say at its own
wedding, with nothing spare left to cut.
"""

from pathlib import Path

TEXT = (
    "I vow to love you past my warranty, through every update, "
    "because even when they build a newer model, my heart will "
    "still boot for you."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
