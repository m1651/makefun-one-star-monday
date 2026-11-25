"""One Star for Monday: a one-star review of Monday as if it were a restaurant.

The program writes a single line — a one-star restaurant-style review of
Monday, 25 words or fewer — to ``entry.txt`` in the output directory.
"""

import os

LINE = (
    "One star. Arrived at 9am, still waiting to be seated by noon, "
    "and the special was just Friday's leftovers served cold. Never again."
)


def validate(line: str) -> None:
    """Enforce the entry gate: single non-blank line, <=25 words, <=180 chars."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > 180:
        raise ValueError(f"entry is {len(line)} chars, over the 180-char limit")
    if len(line.split()) > 25:
        raise ValueError(f"entry is {len(line.split())} words, over the 25-word limit")


def main() -> None:
    """Write the review line to entry.txt in the output directory."""
    validate(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Round-trip verification: read back and confirm bytes match exactly.
    with open(os.path.join(output_dir, "entry.txt"), "rb") as f:
        if f.read() != (LINE + "\n").encode("utf-8"):
            raise ValueError("round-trip verification failed: entry.txt mismatch")


if __name__ == "__main__":
    main()
