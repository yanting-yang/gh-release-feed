"""GitHub API utilities."""

import requests


def fetch_github_releases(owner: str, repo: str, per_page: int = 30) -> list:
    """Fetch releases from GitHub API.

    Args:
        owner: Repository owner/organization
        repo: Repository name
        per_page: Number of releases to fetch (max 100)

    Returns:
        List of release dictionaries from GitHub API
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/releases"
    params = {"per_page": per_page}
    headers = {"Accept": "application/vnd.github+json"}

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()
