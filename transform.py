"""
transform.py
Reads raw JIRA issue data and converts it into a clean JSONL corpus suitable for LLM training.
"""

import json
import os
import argparse
from datetime import datetime

def clean_text(text):
    """Remove extra whitespace and newlines."""
    if not text:
        return ""
    return " ".join(text.split())

def transform_issue(issue, project_name):
    """Extract and structure issue fields."""
    fields = issue.get("fields", {})
    comments = fields.get("comment", {}).get("comments", [])

    combined_comments = " ".join(
        [clean_text(c.get("body", "")) for c in comments]
    )

    description = clean_text(fields.get("description", ""))

    # Derived LLM task examples
    derived = {
        "summary_task": f"Summarize this issue: {description[:400]}",
        "classification_task": f"Classify the issue priority and type: {description[:400]}",
        "qna_task": f"Question: What is this issue about?\nAnswer: {fields.get('summary', '')}"
    }

    return {
        "id": issue.get("id"),
        "key": issue.get("key"),
        "project": project_name,
        "summary": clean_text(fields.get("summary", "")),
        "description": description,
        "comments": combined_comments,
        "created": fields.get("created"),
        "updated": fields.get("updated"),
        "derived": derived
    }

def transform_all(input_folder="data", output_file="data/llm_corpus.jsonl"):
    """Merge and transform all project issue files."""
    os.makedirs("data", exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as out_f:
        for file in os.listdir(input_folder):
            if not file.endswith("_issues.jsonl"):
                continue
            project_name = file.split("_")[0].upper()
            print(f"🔄 Transforming {project_name}...")
            with open(os.path.join(input_folder, file), "r", encoding="utf-8") as in_f:
                for line in in_f:
                    try:
                        issue = json.loads(line)
                        clean_issue = transform_issue(issue, project_name)
                        out_f.write(json.dumps(clean_issue) + "\n")
                    except Exception as e:
                        print(f"⚠️ Error processing issue: {e}")
                        continue
    print(f"\n✅ Transformation complete. Output saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transform Apache Jira issues into LLM-ready corpus.")
    parser.add_argument("--in-folder", default="data", help="Input folder containing *_issues.jsonl files")
    parser.add_argument("--out", default="data/llm_corpus.jsonl", help="Output JSONL file path")
    args = parser.parse_args()

    transform_all(args.in_folder, args.out)
