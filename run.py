#!/usr/bin/env python3
"""Generate RSS feeds for all configured GitHub repositories."""

from pathlib import Path

from config import REPOS
from lib import fetch_github_releases, create_rss_feed, save_feed

OUTPUT_DIR = Path(__file__).parent / "output"


def generate_feed(owner: str, repo: str, per_page: int) -> None:
    """Generate RSS feed for a single repository."""
    print(f"Fetching releases for {owner}/{repo}...")
    releases = fetch_github_releases(owner, repo, per_page=per_page)
    print(f"Found {len(releases)} releases")

    rss_feed = create_rss_feed(
        releases=releases,
        title=f"{owner}/{repo} Releases",
        link=f"https://github.com/{owner}/{repo}/releases",
        description=f"Latest releases from {owner}/{repo} on GitHub",
    )

    xml_path = save_feed(
        name=f"{owner}_{repo}",
        rss_content=rss_feed,
        output_dir=OUTPUT_DIR,
    )

    print(f"RSS feed saved to {xml_path}")


def main():
    """Generate feeds for all configured repositories."""
    print("=" * 50)
    print("Generating RSS feeds...")
    print("=" * 50)

    for owner, repo, per_page in REPOS:
        print(f"\n[{owner}/{repo}]")
        try:
            generate_feed(owner, repo, per_page)
        except Exception as e:
            print(f"Error: {e}")

    print("\n" + "=" * 50)
    print("Done!")
    print("=" * 50)


if __name__ == "__main__":
    main()
