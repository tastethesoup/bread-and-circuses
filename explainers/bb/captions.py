"""WebVTT captions and chapters from the locked word timings."""

from __future__ import annotations

import json
from pathlib import Path

MAX_LINE = 42
MAX_LINES = 2


def load_words(path: Path) -> list[dict]:
    data = json.loads(path.read_text())
    words = []
    for word in data["words"]:
        if "word" not in word or "start" not in word or "end" not in word:
            raise ValueError(f"timing row missing fields: {word!r}")
        # A trailing unaligned backtick in the It's Over timings is not speech.
        if not any(ch.isalnum() for ch in word["word"]):
            continue
        words.append(word)
    return words


def _wrap(text: str) -> list[str]:
    lines: list[str] = []
    current = ""
    for word in text.split():
        trial = word if not current else f"{current} {word}"
        if len(trial) <= MAX_LINE:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def pack_cues(words: list[dict]) -> list[dict]:
    """Cues of at most two lines, each at most 42 characters.

    A cue breaks on a sentence end once it is reasonably full, and on a
    pause longer than 0.8 seconds. Words are copied from the timing file
    with no spelling changes.
    """
    cues: list[list[dict]] = []
    buf: list[dict] = []

    def flush():
        if buf:
            cues.append(list(buf))
            buf.clear()

    for index, word in enumerate(words):
        trial = buf + [word]
        lines = _wrap(" ".join(item["word"] for item in trial))
        too_big = len(lines) > MAX_LINES or any(len(line) > MAX_LINE for line in lines)
        if too_big and buf:
            flush()
            buf.append(word)
        else:
            buf.append(word)
        if not buf:
            continue
        nxt = words[index + 1] if index + 1 < len(words) else None
        pause = (nxt["start"] - word["end"]) if nxt else 0.0
        text = " ".join(item["word"] for item in buf)
        sentence = word["word"].endswith((".", "?", "!"))
        full = len(text) >= 24
        if nxt is None or (sentence and full) or (pause > 0.8 and (full or sentence)):
            flush()
    flush()

    packed = []
    for index, group in enumerate(cues):
        text = " ".join(item["word"] for item in group)
        lines = _wrap(text)
        if len(lines) > MAX_LINES or any(len(line) > MAX_LINE for line in lines):
            raise ValueError(f"cue exceeds the line budget: {text!r}")
        start = float(group[0]["start"])
        end = float(group[-1]["end"])
        if end <= start:
            end = start + 0.24
        if index + 1 < len(cues):
            nxt_start = float(cues[index + 1][0]["start"])
            if end > nxt_start:
                end = max(start + 0.08, nxt_start - 0.01)
        packed.append({"start": start, "end": end, "lines": lines})
    return packed


def stamp(t: float) -> str:
    if t < 0:
        t = 0.0
    hours = int(t // 3600)
    minutes = int((t % 3600) // 60)
    seconds = t % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:06.3f}"


def cues_vtt(cues: list[dict]) -> str:
    parts = ["WEBVTT", ""]
    for cue in cues:
        parts.append(f"{stamp(cue['start'])} --> {stamp(cue['end'])}")
        parts.append("\n".join(cue["lines"]))
        parts.append("")
    return "\n".join(parts) + "\n"


def chapters_vtt(sections: list[tuple[str, float]], duration: float) -> str:
    parts = ["WEBVTT", ""]
    for index, (title, start) in enumerate(sections):
        end = sections[index + 1][1] if index + 1 < len(sections) else duration
        parts.append(f"{stamp(start)} --> {stamp(end)}")
        parts.append(title)
        parts.append("")
    return "\n".join(parts) + "\n"


def write_pair(words_path: Path, captions_path: Path, chapters_path: Path, sections, duration: float):
    cues = pack_cues(load_words(words_path))
    captions_path.write_text(cues_vtt(cues))
    chapters_path.write_text(chapters_vtt(sections, duration))
    return len(cues)
