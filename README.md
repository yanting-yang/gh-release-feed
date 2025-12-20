# 📡 GitHub Releases to RSS

Convert GitHub releases to RSS feeds.

## 🚀 Usage

1. 🍴 **Fork** this repository
2. ✏️ **Edit** `config.py` to add your repositories:
   ```python
   REPOS = [
       ("owner", "repo", 5),  # (owner, repo, number_of_releases)
   ]
   ```
3. 🌐 **Enable GitHub Pages** (Settings → Pages → Source: `main` branch)
4. ✅ **Done!** Feeds auto-update daily, or trigger manually from Actions tab

📬 Your RSS feeds will be available at:
```
https://<username>.github.io/<fork-name>/output/<owner>_<repo>.xml
```

## 📄 License

MIT
