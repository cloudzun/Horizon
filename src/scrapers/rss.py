"""RSS feed scraper implementation."""

import calendar
import hashlib
import asyncio
import logging
import os
import re
from datetime import datetime, timezone
from typing import List
from email.utils import parsedate_to_datetime
import httpx
import feedparser

from .base import BaseScraper
from ..extractors import ExtractorRegistry
from ..models import ContentItem, SourceType, RSSSourceConfig

logger = logging.getLogger(__name__)


class RSSScraper(BaseScraper):
    """Scraper for RSS/Atom feeds."""

    def __init__(self, sources: List[RSSSourceConfig], http_client: httpx.AsyncClient):
        """Initialize RSS scraper.

        Args:
            sources: List of RSS feed configurations
            http_client: Shared async HTTP client
        """
        super().__init__({"sources": sources}, http_client)
        self._extractors = ExtractorRegistry()

    async def fetch(self, since: datetime) -> List[ContentItem]:
        """Fetch RSS feed items.

        Args:
            since: Only fetch items published after this time

        Returns:
            List[ContentItem]: Fetched content items
        """
        sources = [s for s in self.config["sources"] if s.enabled]
        if not sources:
            return []

        # Fetch feeds concurrently, bounded by a semaphore.
        semaphore = asyncio.Semaphore(4)

        async def _fetch_one(source: RSSSourceConfig) -> List[ContentItem]:
            async with semaphore:
                return await self._fetch_feed(source, since)

        results = await asyncio.gather(*[_fetch_one(s) for s in sources])
        return [item for items in results for item in items]

    async def _fetch_feed(
        self,
        source: RSSSourceConfig,
        since: datetime
    ) -> List[ContentItem]:
        """Fetch items from a single RSS feed.

        Args:
            source: RSS feed configuration
            since: Only fetch items after this time

        Returns:
            List[ContentItem]: Feed content items
        """
        try:
            # Expand environment variables in URL (e.g. ${LWN_TOKEN})
            feed_url = re.sub(
                r'\$\{(\w+)\}',
                lambda m: os.environ.get(m.group(1), m.group(0)).strip(),
                str(source.url),
            )

            # Fetch feed content
            response = await self.client.get(feed_url, follow_redirects=True)
            response.raise_for_status()

            # Parse feed
            feed = feedparser.parse(response.text)
        except httpx.HTTPError as e:
            logger.warning("Error fetching RSS feed %s: %s", source.name, e)
            self.record_error(f"RSS feed {source.name}: {e}")
            return []
        except Exception as e:
            logger.warning("Error parsing RSS feed %s: %s", source.name, e)
            self.record_error(f"RSS feed {source.name}: {e}")
            return []

        # Generate unique, stable ID from feed URL and entry ID
        feed_id = str(source.url).split("//")[1].replace("/", "_")
        extractor = None
        if source.content_extractor:
            extractor = self._extractors.get(source.content_extractor)
        semaphore = asyncio.Semaphore(4)

        async def _build_item(entry: dict, published_at: datetime) -> ContentItem:
            entry_id = entry.get("id", entry.get("link", ""))
            entry_hash = hashlib.sha256(
                str(entry_id).encode("utf-8")
            ).hexdigest()[:16]

            content = self._extract_content(entry)
            if extractor:
                link = entry.get("link", "")
                if link:
                    async with semaphore:
                        full = await extractor.extract(link, self.client)
                    if full:
                        content = full

            return ContentItem(
                id=self._generate_id("rss", feed_id, entry_hash),
                source_type=SourceType.RSS,
                title=entry.get("title", "Untitled"),
                url=entry.get("link", str(source.url)),
                content=content,
                author=entry.get("author", source.name),
                published_at=published_at,
                metadata={
                    "feed_name": source.name,
                    "category": source.category,
                    "tags": [tag.term for tag in entry.get("tags", [])],
                }
            )

        tasks = []
        for entry in feed.entries:
            published_at = self._parse_date(entry)
            if not published_at or published_at < since:
                continue
            tasks.append(_build_item(entry, published_at))

        items = await asyncio.gather(*tasks)
        return list(items)

    def _parse_date(self, entry: dict) -> datetime:
        """Parse publication date from feed entry.

        Args:
            entry: Feed entry data

        Returns:
            datetime: Parsed publication date or None
        """
        # Try different date fields
        for field in ["published", "updated", "created"]:
            if field in entry:
                try:
                    # Try parsing structured time first
                    if f"{field}_parsed" in entry and entry[f"{field}_parsed"]:
                        return datetime.fromtimestamp(
                            calendar.timegm(entry[f"{field}_parsed"]),
                            tz=timezone.utc
                        )
                    # Fallback to string parsing
                    date_str = entry[field]
                    return parsedate_to_datetime(date_str)
                except Exception:
                    continue

        return None

    def _extract_content(self, entry: dict) -> str:
        """Extract text content from feed entry.

        Args:
            entry: Feed entry data

        Returns:
            str: Extracted text content
        """
        # Try different content fields
        if "summary" in entry:
            return entry.summary
        elif "description" in entry:
            return entry.description
        elif "content" in entry and entry.content:
            # content is usually a list
            return entry.content[0].get("value", "")

        return ""
