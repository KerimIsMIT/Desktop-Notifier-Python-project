# Desktop-Notifier-Python-project
A Python desktop notifier app that fetches top news headlines and shows them as desktop notifications.

# Desktop Notifier Python

A simple Python desktop notifier that fetches top news headlines from RSS feeds and displays them as desktop notifications.

## Files

- `topnews.py`: Fetches and parses news RSS feeds.
- `desktop_notifier.py`: Displays notifications on desktop.

## Requirements

- Python 3
- `requests` library
- `notify2` library (Linux) **or** `plyer` (Windows)

Install dependencies:

```bash
# For Linux
pip install requests notify2

# For Windows
pip install requests plyer
