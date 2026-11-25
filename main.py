"""One Star for Monday: a one-star review of Monday, as if it were a restaurant.

Writes a single line of plain text to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when the variable is unset).
"""

import os

REVIEW = (
    "One star. The waiter sat me at a table called Monday, served cold "
    "coffee, then charged me my whole weekend."
)


def validate_review(text: str) -> str:
    """Check the review against the gate before anything is written."""
    text.encode("utf-8")  # raises if not valid UTF-8
    if not 1 <= len(text) <= 180:
        raise ValueError(f"review must be 1-180 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("review must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    if len(text.split()) > 25:
        raise ValueError(f"review must be at most 25 words, got {len(text.split())}")
    return text


def write_entry(text: str, out_dir: str) -> str:
    """Validate the review, then write it as entry.txt in out_dir."""
    line = validate_review(text)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    return path


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(REVIEW, out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
