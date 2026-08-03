"""Daily summary generation — pure programmatic rendering."""

import html
import re
from urllib.parse import urlsplit
from typing import List, Dict

from ..models import ContentItem


_CJK = r"[\u4e00-\u9fff\u3400-\u4dbf]"
_ASCII = r"[A-Za-z0-9]"


_MD_ESCAPE_RE = re.compile(r'([\\`*_{}\[\]()#+\-.!|~])')


def _md_escape(text: str) -> str:
    """Escape Markdown syntax and HTML in untrusted text.

    Turns scraped/AI-generated text into inert plain text so it cannot inject
    raw HTML or forge links (e.g. ``[x](javascript:...)``) into the report.
    """
    if not text:
        return text
    # Neutralize HTML first (ampersand before other entities).
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = text.replace('"', "&quot;")
    # Escape Markdown syntax so user/AI text can't create headings, links,
    # images, or other constructs.
    return _MD_ESCAPE_RE.sub(r"\\\1", text)


def _safe_url(url: str) -> str:
    """Only allow http/https destinations in rendered links."""
    try:
        scheme = urlsplit(url).scheme.lower()
    except ValueError:
        return "#"
    return url if scheme in ("http", "https") else "#"


def _pangu(text: str) -> str:
    """Insert a space between CJK and ASCII letters/digits (Pangu spacing)."""
    text = re.sub(rf"({_CJK})({_ASCII})", r"\1 \2", text)
    text = re.sub(rf"({_ASCII})({_CJK})", r"\1 \2", text)
    return text


LABELS = {
    "en": {
        "header": "Horizon Daily",
        "source": "Source",
        "background": "Background",
        "discussion": "Discussion",
        "references": "References",
        "tags": "Tags",
        "empty_body": (
            "No significant developments today. This might indicate:\n"
            "- A quiet day in your tracked sources\n"
            "- The AI score threshold is too high\n"
            "- Your information sources need expansion\n\n"
            "Consider:\n"
            "1. Lowering the `ai_score_threshold` in config.json\n"
            "2. Adding more diverse information sources\n"
            "3. Checking if the AI model is working correctly\n"
        ),
    },
    "zh": {
        "header": "Horizon 每日速递",
        "source": "来源",
        "background": "背景",
        "discussion": "社区讨论",
        "references": "参考链接",
        "tags": "标签",
        "empty_body": (
            "今日暂无重要动态，可能原因：\n"
            "- 今天关注的信息源较平静\n"
            "- AI 评分阈值设置过高\n"
            "- 信息源种类有待扩充\n\n"
            "建议：\n"
            "1. 在 config.json 中降低 `ai_score_threshold`\n"
            "2. 添加更多多样化的信息源\n"
            "3. 检查 AI 模型是否正常工作\n"
        ),
    },
}


class DailySummarizer:
    """Generates daily Markdown summaries from pre-analyzed content items."""

    def __init__(self):
        pass

    async def generate_summary(
        self,
        items: List[ContentItem],
        date: str,
        total_fetched: int,
        language: str = "en",
    ) -> str:
        """Generate daily summary in Markdown format.

        Items are rendered in score-descending order (already sorted by orchestrator).

        Args:
            items: High-scoring content items (already enriched)
            date: Date string (YYYY-MM-DD)
            total_fetched: Total number of items fetched before filtering
            language: Output language, either "en" or "zh"

        Returns:
            str: Markdown formatted summary
        """
        labels = LABELS.get(language, LABELS["en"])

        if not items:
            return self._generate_empty_summary(date, total_fetched, labels)

        header = (
            f"# {labels['header']} - {date}\n\n"
            f"> 📅 {date} · 从 {total_fetched} 条资讯中精选出 {len(items)} 条重要内容\n\n"
            "---\n\n"
        )

        # TOC
        toc_entries = []
        for i, item in enumerate(items):
            t = _md_escape(item.metadata.get(f"title_{language}") or item.title)
            if language == "zh":
                t = _pangu(t)
            score = item.ai_score or 0
            toc_entries.append(
                f"{i + 1}. [{t}](#item-{i + 1}) "
                f'<span class="score-badge {self._score_class(score)}">'
                f"{score:.1f}</span>"
            )
        toc = "\n".join(toc_entries) + "\n\n---\n\n"

        parts = [self._format_item(item, labels, language, i + 1) for i, item in enumerate(items)]

        return header + toc + "".join(parts)

    @staticmethod
    def _score_class(score: float) -> str:
        """Map a 0-10 score to a CSS badge class."""
        s = score or 0
        if s >= 9:
            return "score-high"
        if s >= 7:
            return "score-mid"
        if s >= 5:
            return "score-low"
        return "score-none"

    def _format_item(self, item: ContentItem, labels: dict, language: str, index: int) -> str:
        """Format a single ContentItem as semantic HTML.

        Text is HTML-escaped (not markdown-escaped) because items are emitted
        as raw HTML blocks, so markdown backslash escapes would be visible.
        """
        title = item.metadata.get(f"title_{language}") or item.title
        url = _safe_url(str(item.url))
        score = item.ai_score or 0
        meta = item.metadata

        summary = (
            meta.get(f"detailed_summary_{language}")
            or meta.get("detailed_summary")
            or item.ai_summary
            or ""
        )
        background = meta.get(f"background_{language}") or meta.get("background") or ""
        discussion = (
            meta.get(f"community_discussion_{language}")
            or meta.get("community_discussion")
            or ""
        )

        if language == "zh":
            title = _pangu(title)
            summary = _pangu(summary)
            background = _pangu(background)
            discussion = _pangu(discussion)

        title = html.escape(title, quote=True)
        summary = html.escape(summary)
        background = html.escape(background)
        discussion = html.escape(discussion)

        # Source chips: type / name / time
        source_type = item.source_type.value
        chips = [f'<span class="source-chip chip-{source_type}">{source_type}</span>']
        if meta.get("subreddit"):
            chips.append(
                f'<span class="source-name">r/{html.escape(str(meta["subreddit"]))}</span>'
            )
        elif meta.get("feed_name"):
            chips.append(
                f'<span class="source-name">{html.escape(str(meta["feed_name"]))}</span>'
            )
        else:
            chips.append(
                f'<span class="source-name">{html.escape(item.author or "unknown")}</span>'
            )
        if item.published_at:
            day = item.published_at.strftime("%d").lstrip("0")
            chips.append(
                f'<span class="news-time">{item.published_at.strftime(f"%b {day}, %H:%M")}</span>'
            )
        meta_html = f'<div class="news-meta">{"".join(chips)}</div>'

        lines = [
            f'<a id="item-{index}"></a>',
            '<article class="news-item">',
            f'<h2 class="news-title"><a href="{html.escape(url, quote=True)}">{title}</a>'
            f'<span class="score-badge {self._score_class(score)}">{score:.1f}</span></h2>',
            meta_html,
            f'<p class="news-summary">{summary}</p>',
        ]

        if background:
            lines.append(
                f'<div class="news-background"><strong>{labels["background"]}</strong> '
                f"{background}</div>"
            )

        sources = meta.get("sources") or []
        if sources:
            items_html = "".join(
                f'<li><a href="{html.escape(_safe_url(s["url"]), quote=True)}">'
                f'{html.escape(str(s["title"]), quote=True)}</a></li>\n'
                for s in sources
            )
            lines.append(
                f'<details class="news-refs"><summary>{html.escape(labels["references"])}</summary>\n'
                f"<ul>\n{items_html}</ul>\n</details>"
            )

        if discussion:
            lines.append(
                f'<div class="news-discussion"><strong>{labels["discussion"]}</strong> '
                f"{discussion}</div>"
            )

        if item.ai_tags:
            tags_html = " ".join(
                f'<span class="tag">#{html.escape(str(t).replace("`", ""))}</span>'
                for t in item.ai_tags
            )
            lines.append(f'<div class="news-tags">{tags_html}</div>')

        lines.append("</article>")
        lines.append("<hr>")
        return "\n".join(lines) + "\n\n"

    def _generate_empty_summary(self, date: str, total_fetched: int, labels: dict) -> str:
        """Generate summary when no high-scoring items were found."""
        return (
            f"# {labels['header']} - {date}\n\n"
            f"> Analyzed {total_fetched} items, but none met the importance threshold.\n\n"
            + labels["empty_body"]
        )
