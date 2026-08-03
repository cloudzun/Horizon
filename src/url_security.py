"""SSRF-safe HTTP URL validation and request execution."""

from __future__ import annotations

import asyncio
import ipaddress
import socket
from urllib.parse import urlsplit

import httpx


class UnsafeURLError(ValueError):
    """Raised when a URL may target a non-public network resource."""


def validate_http_url(url: str) -> str:
    """Validate the non-network portions of an HTTP(S) URL."""
    try:
        parsed = urlsplit(url)
        port = parsed.port
    except ValueError as exc:
        raise UnsafeURLError(f"Invalid URL: {exc}") from exc

    if parsed.scheme.lower() not in {"http", "https"}:
        raise UnsafeURLError("URL must use http or https")
    if not parsed.hostname:
        raise UnsafeURLError("URL has no hostname")
    if parsed.username is not None or parsed.password is not None:
        raise UnsafeURLError("URL must not contain embedded credentials")
    if port is not None and not 1 <= port <= 65535:
        raise UnsafeURLError("URL port is out of range")

    hostname = parsed.hostname.rstrip(".").lower()
    if hostname == "localhost" or hostname.endswith(".localhost"):
        raise UnsafeURLError("localhost destinations are not allowed")
    return url


async def _resolve_hostname(hostname: str, port: int) -> set[str]:
    try:
        literal = ipaddress.ip_address(hostname)
    except ValueError:
        try:
            results = await asyncio.to_thread(
                socket.getaddrinfo,
                hostname,
                port,
                type=socket.SOCK_STREAM,
            )
        except socket.gaierror as exc:
            raise UnsafeURLError(f"Could not resolve hostname: {hostname}") from exc
        return {str(result[4][0]) for result in results}
    return {str(literal)}


def _is_global(ip: str) -> bool:
    try:
        addr = ipaddress.ip_address(ip)
    except ValueError:
        return False
    return (
        not addr.is_private
        and not addr.is_loopback
        and not addr.is_link_local
        and not addr.is_reserved
        and not addr.is_multicast
        and not addr.is_unspecified
    )


async def validate_public_http_url(url: str) -> str:
    """Validate a URL and require its hostname to resolve only to public IPs."""
    validate_http_url(url)
    parsed = urlsplit(url)
    hostname = parsed.hostname.rstrip(".").lower()
    port = parsed.port or (443 if parsed.scheme.lower() == "https" else 80)
    addresses = await _resolve_hostname(hostname, port)
    if not addresses or not all(_is_global(ip) for ip in addresses):
        raise UnsafeURLError(f"Destination resolves to a non-public address: {hostname}")
    return url


async def safe_request(
    client: httpx.AsyncClient,
    method: str,
    url: str,
    **kwargs,
) -> httpx.Response:
    """Perform an HTTP request after validating the URL is public."""
    await validate_public_http_url(url)
    return await client.request(method, url, **kwargs)
