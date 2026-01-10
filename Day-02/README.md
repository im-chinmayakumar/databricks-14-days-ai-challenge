# Day 2 – Apache Spark Fundamentals 🚀

## 📌 Overview
Day 2 focuses on understanding **Apache Spark fundamentals** and applying them using **PySpark on Databricks**.

---

## 📘 What I Learned

- **Spark Architecture**  
  Driver plans the execution, Executors process data in parallel, and DAG optimizes the workflow.

- **DataFrames vs RDDs**  
  DataFrames are higher-level, optimized, and preferred over RDDs for most use cases.

- **Lazy Evaluation**  
  Spark delays execution until an action is triggered, enabling query optimization.

- **Notebook Magic Commands**  
  `%python`, `%sql`, and `%fs` enable multi-language execution in Databricks notebooks.

---

## 🛠️ Hands-On Tasks

- Uploaded a sample e-commerce dataset
- Loaded CSV data into a Spark DataFrame
- Applied transformations:
  - `select`
  - `filter`
  - `groupBy`
  - `orderBy`
- Exported the processed results

---

## 🧪 Code Implementation

The complete PySpark implementation is available here:

📄 **`day2_spark_fundamentals.py`**

Key operations performed in the script:
- Reading CSV data using Spark
- Data selection and filtering
- Aggregation using `groupBy`
- Sorting and extracting insights

---

## 🎯 Key Takeaways

- Spark enables fast, distributed data processing
- DataFrames improve performance and developer productivity
- Lazy evaluation plays a key role in Spark optimization

---

## 🔧 Tools & Technologies

- Databricks
- Apache Spark
- PySpark

---

## 📅 Challenge Progress
- **Challenge:** Databricks 14 Days AI Challenge  
- **Day Completed:** Day 2
