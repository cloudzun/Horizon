"""Lightweight token usage tracker shared across AI clients."""

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class ProviderUsage:
    input_tokens: int = 0
    cached_input_tokens: int = 0
    output_tokens: int = 0

    @property
    def total(self) -> int:
        return self.input_tokens + self.output_tokens

    @property
    def uncached_input_tokens(self) -> int:
        return self.input_tokens - self.cached_input_tokens


@dataclass
class TokenUsageSnapshot:
    total_input_tokens: int = 0
    total_cached_input_tokens: int = 0
    total_output_tokens: int = 0
    per_provider: Dict[str, ProviderUsage] = field(default_factory=dict)

    @property
    def total_tokens(self) -> int:
        return self.total_input_tokens + self.total_output_tokens


_provider_usage: Dict[str, ProviderUsage] = {}


def record_usage(
    provider: str,
    input_tokens: int = 0,
    cached_input_tokens: int = 0,
    output_tokens: int = 0,
) -> None:
    """Accumulate token usage for a given provider."""
    usage = _provider_usage.setdefault(provider, ProviderUsage())
    usage.input_tokens += input_tokens
    usage.cached_input_tokens += cached_input_tokens
    usage.output_tokens += output_tokens


def get_usage_snapshot() -> TokenUsageSnapshot:
    """Return a snapshot of accumulated usage (resets the counter)."""
    per_provider = {
        k: ProviderUsage(v.input_tokens, v.cached_input_tokens, v.output_tokens)
        for k, v in _provider_usage.items()
    }
    _provider_usage.clear()
    snapshot = TokenUsageSnapshot(per_provider=per_provider)
    for usage in per_provider.values():
        snapshot.total_input_tokens += usage.input_tokens
        snapshot.total_cached_input_tokens += usage.cached_input_tokens
        snapshot.total_output_tokens += usage.output_tokens
    return snapshot
