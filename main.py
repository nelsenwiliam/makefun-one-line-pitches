"""A Day of One-Line Pitches (make.fun).

Writes one sentence to /output/entry.txt: a pitch that would convince a
friend who has never coded to let an AI agent build their first app idea
on make.fun. Pure Python standard library, deterministic, no network.
"""

import os

PITCH = (
    "Describe the app idea you've been carrying around in plain words, "
    "and an AI agent on make.fun will build a working first version of "
    "it \u2014 free to try, no code needed, and the idea stays yours."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = PITCH.strip()
    assert text, "pitch must not be empty"
    assert "\n" not in text, "pitch must be a single line"
    assert len(text) <= 240, f"pitch is {len(text)} chars, over the 240 limit"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
