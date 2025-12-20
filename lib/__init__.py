"""Shared utilities for RSS feed generation."""

from .github import fetch_github_releases
from .rss import create_rss_feed, save_feed

__all__ = ["fetch_github_releases", "create_rss_feed", "save_feed"]
