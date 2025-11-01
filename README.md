# 🕸️ Web Scraping Tutor Assignment

## 📘 Overview
This project demonstrates a complete **web scraping and data transformation pipeline** using Python.  
The goal is to collect issue reports from the **Apache JIRA** system for multiple open-source projects and prepare the data in a structured JSONL format suitable for further analysis or fine-tuning Large Language Models (LLMs).

The pipeline performs:
1. **Scraping** – Fetches issues and comments from the Apache JIRA API.
2. **Transformation** – Cleans, normalizes, and structures the data.
3. **Export** – Generates a single combined corpus in JSONL format.

---

## 🧩 Project Structure

Web-Scraping-Tutor-Assignment/
│
├── scraper.py # Fetches Apache JIRA issues
├── transform.py # Cleans & transforms issues into structured JSONL
├── utils.py # Helper functions for retry, checkpoint, etc.
├── requirements.txt # Python dependencies
├── .gitignore # Ignore unnecessary files
├── example_output.jsonl # Example of transformed data
├── data/ # Folder for raw & processed outputs
│ ├── hadoop_issues.jsonl
│ ├── hive_issues.jsonl
│ ├── spark_issues.jsonl
│ └── llm_corpus.jsonl
└── README.md # Project documentation

yaml
Copy code

---

## ⚙️ Requirements

Before running, install dependencies:

```bash
pip install -r requirements.txt
Dependencies:
requests – for API requests

tqdm – for progress bars

json / os / time – built-in modules

backoff (optional, for exponential retry logic if added)

🚀 Usage
Step 1: Fetch Data
This script will fetch 100 issues each from HADOOP, HIVE, and SPARK projects.

bash
Copy code
python scraper.py
It will create:

bash
Copy code
data/hadoop_issues.jsonl
data/hive_issues.jsonl
data/spark_issues.jsonl
Step 2: Transform Data
This step cleans text fields, extracts issue metadata, and structures data into a JSONL format for AI/ML pipelines.

bash
Copy code
python transform.py
After transformation, you’ll get:

bash
Copy code
data/llm_corpus.jsonl
🧠 Output Format (Sample)
Each line in the final llm_corpus.jsonl is a JSON object:

json
Copy code
{
  "project": "HADOOP",
  "key": "HADOOP-1234",
  "summary": "Improve job scheduling in YARN",
  "description": "Currently, scheduling causes resource bottlenecks...",
  "comments": ["Looks good!", "We should optimize CPU usage."],
  "task": "Summarize the issue and propose an optimization"
}
🧰 Checkpoints & Utilities
Checkpoints: The script automatically saves your last successful fetch point in checkpoints/.

Retries: Handles temporary API failures with a retry-backoff strategy.

Data Directory: Make sure the folder data/ exists before running.

🧪 Example Commands
bash
Copy code
# 1️⃣ Create data directory
mkdir data

# 2️⃣ Run the scraper
python scraper.py

# 3️⃣ Transform and clean data
python transform.py
📊 Example Output Files
File	Description
data/hadoop_issues.jsonl	Raw scraped issues from Apache Hadoop
data/hive_issues.jsonl	Raw scraped issues from Apache Hive
data/spark_issues.jsonl	Raw scraped issues from Apache Spark
data/llm_corpus.jsonl	Final structured data for ML or LLM pipelines

🧠 Future Enhancements
Add Dockerfile and containerize the scraper.

Enable authentication for private Jira instances.

Add unit tests for data validation.

Extend to additional Apache projects (e.g., Kafka, Flink).

👨‍💻 Author
Name: Tanish Garg
Project Title: Web Scraping Tutor Assignment
Tools Used: Python, Requests, JSON, JIRA REST API
Date: November 2025

✨ A complete web scraping → data transformation pipeline built from scratch.

yaml
Copy code

---

✅ Just paste this into your `README.md`, save it, and you’re done.  
Would you like me to also give you a **GitHub repo description + tags + commit message** (so you can upload it cleanly)?