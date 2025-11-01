"""
scraper.py
Fetches Apache JIRA issues & comments using the public REST API (latest version).
"""

import requests
import json
import time
import argparse
from utils import retry_request, save_checkpoint, load_checkpoint

JIRA_API = "https://issues.apache.org/jira/rest/api/latest/search"


def fetch_issues(project, start=0, max_results=50, total_limit=200):
    """Fetch issues for a single project."""
    all_issues = []
    start_at = load_checkpoint(f"checkpoint_{project}.json") or start

    while start_at < total_limit:
        jql_query = f"project={project} ORDER BY created DESC"

        payload = {
            "jql": jql_query,
            "startAt": start_at,
            "maxResults": max_results,
            "fields": ["summary", "description", "created", "updated", "comment"],
        }

        print(f"\n📦 Fetching {project} issues {start_at} - {start_at + max_results}")
        headers = {"Content-Type": "application/json"}
        response = retry_request(JIRA_API, method="POST", json=payload, headers=headers)

        if not response:
            print(f"❌ Failed to fetch {project}. Stopping this project.")
            break

        data = response.json()
        if "errorMessages" in data:
            print(f"⚠️ Error for {project}: {data['errorMessages']}")
            break

        issues = data.get("issues", [])
        if not issues:
            print(f"✅ No more issues found for {project}.")
            break

        out_file = f"data/{project.lower()}_issues.jsonl"
        with open(out_file, "a", encoding="utf-8") as f:
            for issue in issues:
                f.write(json.dumps(issue) + "\n")

        all_issues.extend(issues)
        start_at += max_results
        save_checkpoint(f"checkpoint_{project}.json", start_at)
        time.sleep(2)

    print(f"✅ Done fetching {len(all_issues)} issues for {project}.")
    return all_issues


def main():
    parser = argparse.ArgumentParser(description="Fetch Apache Jira issues for multiple projects.")
    parser.add_argument("--projects", nargs="+", default=["HADOOP", "HIVE", "SPARK"], help="List of Apache projects")
    parser.add_argument("--max-issues", type=int, default=100, help="Max number of issues per project")
    args = parser.parse_args()

    for project in args.projects:
        fetch_issues(project, total_limit=args.max_issues)


if __name__ == "__main__":
    main()
