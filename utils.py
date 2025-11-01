"""
utils.py
Utility functions for retry logic, checkpoints, and safe HTTP handling.
"""

import json
import os
import time
import requests
from requests.exceptions import RequestException


def retry_request(url, method="GET", params=None, json=None, headers=None, retries=3, delay=2):
    """Handles retries and errors for GET/POST requests."""
    for i in range(retries):
        try:
            if method.upper() == "POST":
                resp = requests.post(url, json=json, headers=headers, timeout=15)
            else:
                resp = requests.get(url, params=params, headers=headers, timeout=15)

            if resp.status_code == 200:
                return resp

            print(f"⚠️ Status {resp.status_code}: {resp.text[:100]}")
        except RequestException as e:
            print(f"⚠️ Network error: {e}")

        time.sleep(delay * (i + 1))

    return None


def save_checkpoint(file_path, state):
    """Saves the current progress to a JSON file so we can resume later."""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump({"start_at": state}, f)


def load_checkpoint(file_path):
    """Loads saved progress if available."""
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("start_at", 0)
    return 0
