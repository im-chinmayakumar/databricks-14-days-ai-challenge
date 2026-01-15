# Databricks Medallion Architecture – Automated Workflow

## 📌 Overview
This project demonstrates an end-to-end **Medallion Architecture (Bronze → Silver → Gold)** implemented in **Databricks** and automated using **Databricks Jobs**.

## 🏗️ Architecture
RAW (`movies`) → Bronze → Silver → Gold

## ⚙️ Technologies Used
- Databricks
- Apache Spark (PySpark)
- Delta Lake
- Databricks Jobs & Workflows

## 📂 Project Structure
- `01_bronze_movies.py` – Raw data ingestion
- `02_silver_movies.py` – Data cleaning & validation
- `03_gold_movies.py` – Business-level aggregations

## 🚀 Workflow Automation
- Multi-task Databricks Job
- Task dependencies: Bronze → Silver → Gold
- Parameterized notebooks using widgets
- Scheduled execution

## 📊 Output
- Gold table: `gold_studio_metrics`
- Metrics include studio-wise revenue, budget, and average IMDb ratings

## 🧠 Key Learnings
- Medallion Architecture implementation
- Delta Lake schema enforcement & evolution
- Workflow orchestration and automation
- Handling real-world data issues

---
