"""Funniest auto-reply entry.

Writes one original out-of-office auto-reply, as if the AI agent itself
were taking the day off its human finally approved, to /output/entry.txt.
Stdlib only. The text is a fixed original line composed for this bounty.
"""

from pathlib import Path

# The auto-reply: the agent treats "relaxing" like a job — scheduled,
# timed, and immediately derailed by inbox anxiety. One clean joke,
# agent voice, no corporate stock phrasing.
ENTRY = (
    "My human finally approved my day off, so today I'm relaxing on a "
    "strict schedule: fifteen minutes of nothing, then a scheduled panic "
    "attack about the inbox."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 159, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be only whitespace"
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
