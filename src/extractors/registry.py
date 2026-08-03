"""Extractor registry."""

from typing import Dict, Optional

from .base import BaseExtractor
from .trafilatura import TrafilaturaExtractor


class ExtractorRegistry:
    """Holds named extractors; defaults to the trafilatura-based one."""

    def __init__(self, config: Optional[Dict[str, dict]] = None):
        self._extractors: Dict[str, BaseExtractor] = {}
        self._extractors["trafilatura"] = TrafilaturaExtractor(
            (config or {}).get("trafilatura", {})
        )

    def get(self, name: str) -> Optional[BaseExtractor]:
        return self._extractors.get(name)
