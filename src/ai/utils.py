"""Shared AI utility functions."""

import json
import re
from typing import Optional


def parse_json_response(response: str) -> Optional[dict]:
    """Try multiple strategies to extract a JSON object from an AI response.

    Returns the parsed dict, or None if all strategies fail.
    """
    text = response.strip()

    # Strategy 1: direct parse
    try:
        return json.loads(text)
    except (json.JSONDecodeError, ValueError):
        pass

    # Strategy 2: extract from ```json ... ``` code block
    if "```json" in text:
        try:
            json_str = text.split("```json")[1].split("```")[0].strip()
            return json.loads(json_str)
        except (json.JSONDecodeError, ValueError, IndexError):
            pass

    # Strategy 3: extract from ``` ... ``` code block
    if "```" in text:
        try:
            json_str = text.split("```")[1].split("```")[0].strip()
            return json.loads(json_str)
        except (json.JSONDecodeError, ValueError, IndexError):
            pass

    # Strategy 4: find the first { ... } block using brace matching
    start = text.find("{")
    if start != -1:
        depth = 0
        for i in range(start, len(text)):
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(text[start : i + 1])
                    except (json.JSONDecodeError, ValueError):
                        break

    # Strategy 5: regex extraction as last resort
    match = re.search(r"\{[\s\S]*\}", text)
    if match:
        try:
            return json.loads(match.group())
        except (json.JSONDecodeError, ValueError):
            pass

    return None


COMMENTS_MARKER = "--- Top Comments ---"


def split_content(content: Optional[str]) -> tuple[str, str]:
    """Separate source content from appended community comments."""
    if not content:
        return "", ""
    if COMMENTS_MARKER not in content:
        return content.strip(), ""
    main, comments = content.split(COMMENTS_MARKER, 1)
    return main.strip(), comments.strip()


def select_content(
    content: str,
    max_chars: int,
    sampling: str = "head-middle-tail",
) -> str:
    """Return a bounded excerpt, preserving a long article's conclusion.

    ``sampling="prefix"`` keeps the naive ``content[:max_chars]`` behavior;
    ``sampling="head-middle-tail"`` (default) keeps an opening excerpt, a
    middle slice and the closing paragraph, so the AI sees both the beginning
    and the conclusion of long-form content.
    """
    text = content.strip()
    if len(text) <= max_chars:
        return text
    if sampling == "prefix":
        return text[:max_chars].rstrip()

    markers = (
        "[Opening excerpt]\n",
        "\n\n[Middle excerpt]\n",
        "\n\n[Closing excerpt]\n",
    )
    available = max_chars - sum(len(marker) for marker in markers)
    opening_size = int(available * 0.4)
    middle_size = int(available * 0.3)
    closing_size = available - opening_size - middle_size
    midpoint = len(text) // 2
    middle_start = max(0, midpoint - middle_size // 2)

    opening = text[:opening_size].rstrip()
    middle = text[middle_start : middle_start + middle_size].strip()
    closing = text[-closing_size:].lstrip()
    return (
        markers[0]
        + opening
        + markers[1]
        + middle
        + markers[2]
        + closing
    )
