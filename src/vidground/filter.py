"""Filter a QA dataset down to visually grounded examples.

Implements the core VidGround filtering idea (paper, Sec. 3 / 4):
a question is *visually grounded* if a strong text-only LLM, given only the
question (and options), cannot reliably answer it. Questions that the LLM
solves without seeing the video are removed.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass
class Example:
    id: str
    question: str
    options: list[str]
    answer: str


def is_visually_grounded(example: Example) -> bool:
    """Return True if the example requires watching the video.

    TODO: implement the text-only LLM probe described in the paper.
    """
    raise NotImplementedError


def filter_dataset(examples: Iterable[Example]) -> list[Example]:
    """Keep only visually grounded examples."""
    return [ex for ex in examples if is_visually_grounded(ex)]
