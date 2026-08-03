"""Content analysis using AI."""

import asyncio
import traceback
from typing import List
from tenacity import retry, stop_after_attempt, wait_exponential
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, MofNCompleteColumn

from .client import AIClient
from .prompts import CONTENT_ANALYSIS_SYSTEM, CONTENT_ANALYSIS_USER
from ..models import ContentItem, sanitize_text
from .utils import parse_json_response, select_content, split_content


class ContentAnalyzer:
    """Analyzes content items using AI to determine importance."""

    def __init__(self, ai_client: AIClient, concurrency: int = 8):
        self.client = ai_client
        self.concurrency = concurrency

    async def analyze_batch(
        self,
        items: List[ContentItem],
        batch_size: int = 10
    ) -> List[ContentItem]:
        analyzed_items = [None] * len(items)
        semaphore = asyncio.Semaphore(self.concurrency)

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            MofNCompleteColumn(),
            transient=True,
        ) as progress:
            task = progress.add_task("Analyzing", total=len(items))

            async def analyze_one(idx: int, item: ContentItem):
                async with semaphore:
                    try:
                        await self._analyze_item(item)
                    except Exception as e:
                        print(f"Error analyzing item {item.id}: {e}")
                        traceback.print_exc()
                        item.ai_score = 0.0
                        item.ai_reason = "Analysis failed"
                        item.ai_summary = item.title
                    analyzed_items[idx] = item
                    progress.advance(task)

            await asyncio.gather(*[analyze_one(i, item) for i, item in enumerate(items)])

        return [item for item in analyzed_items if item is not None]

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(min=2, max=10)
    )
    async def _analyze_item(self, item: ContentItem) -> None:
        """Analyze a single content item."""
        main_text, comments_text = split_content(item.content)
        content_section = f"Content: {select_content(main_text, 800)}"

        discussion_parts = []
        if comments_text:
            discussion_parts.append(
                f"Community Comments:\n{select_content(comments_text, 1500, sampling='prefix')}"
            )

        meta = item.metadata
        engagement_items = []
        if meta.get("score"):
            engagement_items.append(f"score: {meta['score']}")
        if meta.get("descendants"):
            engagement_items.append(f"{meta['descendants']} comments")
        if meta.get("favorite_count"):
            engagement_items.append(f"{meta['favorite_count']} likes")
        if meta.get("retweet_count"):
            engagement_items.append(f"{meta['retweet_count']} retweets")
        if meta.get("reply_count"):
            engagement_items.append(f"{meta['reply_count']} replies")
        if meta.get("views"):
            engagement_items.append(f"{meta['views']} views")
        if meta.get("bookmarks"):
            engagement_items.append(f"{meta['bookmarks']} bookmarks")
        if meta.get("upvote_ratio"):
            engagement_items.append(f"upvote ratio: {meta['upvote_ratio']:.0%}")
        if engagement_items:
            discussion_parts.append(f"Engagement: {', '.join(engagement_items)}")
        if meta.get("discussion_url"):
            discussion_parts.append(f"Discussion: {meta['discussion_url']}")
        if meta.get("community_note"):
            discussion_parts.append(f"Community Note: {meta['community_note']}")

        discussion_section = "\n".join(discussion_parts) if discussion_parts else ""

        user_prompt = CONTENT_ANALYSIS_USER.format(
            title=sanitize_text(item.title),
            source=f"{item.source_type.value}",
            author=sanitize_text(item.author or "Unknown"),
            url=sanitize_text(str(item.url)),
            content_section=sanitize_text(content_section),
            discussion_section=sanitize_text(discussion_section)
        )

        response = await self.client.complete(
            system=CONTENT_ANALYSIS_SYSTEM,
            user=user_prompt,
            temperature=0.3
        )

        result = parse_json_response(response)
        if result is None:
            raise ValueError(f"Invalid JSON response: {response}")

        item.ai_score = float(result.get("score", 0))
        item.ai_reason = result.get("reason", "")
        item.ai_summary = result.get("summary", item.title)
        item.ai_tags = result.get("tags", [])
