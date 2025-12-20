"""Configuration for GitHub release feeds."""

# List of GitHub repositories to fetch releases from
# Format: (owner, repo, per_page)
REPOS = [
    ("pytorch", "pytorch", 5),
    ("huggingface", "transformers", 5),
    ("huggingface", "datasets", 5),
    ("huggingface", "accelerate", 5),
]
