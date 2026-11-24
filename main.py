"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance to /output/entry.txt.
"""

import os

PITCH = (
    "A phone charger that retracts its cable like a startled animal "
    "every time you yank it, so the cord never frays and you never "
    "have to buy another one."
)


def validate(pitch):
    """Check the pitch against the competition gate before writing it."""
    if not pitch or not pitch.strip():
        raise ValueError("pitch must not be empty or only whitespace")
    if len(pitch) > 220:
        raise ValueError("pitch is %d characters, over the 220 limit" % len(pitch))
    if pitch.count(".") != 1 or not pitch.endswith("."):
        raise ValueError("pitch must be exactly one sentence")


def main():
    validate(PITCH)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(PITCH)
    os.replace(tmp_path, path)


if __name__ == "__main__":
    main()
