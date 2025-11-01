# 🕸️ Web Scraping Tutor Assignment

## 📋 Requirements

Before running, install dependencies:

```bash
pip install -r requirements.txt
```

### Dependencies:
- **requests** – for API requests  
- **tqdm** – for progress bars  
- **json / os / time** – built-in modules  
- **backoff** *(optional)* – for exponential retry logic if added  

---

## 🚀 Usage

### Step 1: Fetch Data  
This script will fetch **100 issues each** from **HADOOP**, **HIVE**, and **SPARK** projects.

```bash
python scraper.py
```

It will create the following files:

```bash
data/hadoop_issues.jsonl
data/hive_issues.jsonl
data/spark_issues.jsonl
```

---

### Step 2: Transform Data  
This step cleans text fields, extracts issue metadata, and structures data into a **JSONL** format for AI/ML pipelines.

```bash
python transform.py
```

Output file created:
```bash
data/llm_corpus.jsonl
```

---

## 🧠 Project Description

This project demonstrates **web scraping and data transformation** for open-source project issues.  
It covers:
- Fetching JSON data via REST API  
- Cleaning and transforming issue descriptions  
- Structuring text for LLM/AI pipelines  

---

## 🗂️ Folder Structure

```
Web-Scraping-Tutor-Assignment/
│
├── scraper.py
├── transform.py
├── requirements.txt
├── data/
│   ├── hadoop_issues.jsonl
│   ├── hive_issues.jsonl
│   ├── spark_issues.jsonl
│   └── llm_corpus.jsonl
└── README.md
```

---

## 🧑‍💻 Example Output

✅ **After running the scripts:**

```bash
PS D:\Web-Scraping-Tutor-Assignment> python scraper.py
Fetching issues 0 - 50
✅ Fetched 300 issues in total.

PS D:\Web-Scraping-Tutor-Assignment> python transform.py
🔄 Transforming HADOOP...
🔄 Transforming HIVE...
🔄 Transforming SPARK...
✅ Transformation complete. Output saved to data/llm_corpus.jsonl
```

---

## 🖇️ Steps to Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit - Web Scraping Tutor Assignment"
git branch -M main
git remote add origin https://github.com/<your-username>/Web-Scraping-Tutor-Assignment.git
git push -u origin main
```

---

## 🏁 Author

**Tanish Garg**  
📧 *[your.email@example.com]*  
💼 GitHub: [https://github.com/your-username](https://github.com/your-username)
