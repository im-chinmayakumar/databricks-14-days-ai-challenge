# Day 4 (12/01/26) – Delta Lake Introduction 🚀

## 📌 Overview
Day 4 focused on understanding **Delta Lake**, the storage layer that brings reliability and ACID transactions to data lakes in the Databricks Lakehouse architecture.

---

## 📘 What I Learned

- **What is Delta Lake**  
  Delta Lake adds transactional capabilities and versioning on top of data lakes.

- **ACID Transactions**  
  Ensures reliable reads and writes even with concurrent operations.

- **Schema Enforcement**  
  Prevents incorrect or incompatible data from being written to tables.

- **Delta vs Parquet**  
  Parquet is a file format, while Delta adds transaction logs and data consistency.

---

## 🛠️ Hands-On Tasks

1. Converted CSV data into Delta format  
2. Created Delta tables using PySpark and SQL  
3. Tested schema enforcement with invalid inserts  
4. Handled duplicate and inconsistent data safely  

---

## 🧪 Practice & Implementation

### PySpark – Convert CSV to Delta
```python
# Convert CSV to Delta format
events.write.format("delta") \
    .mode("overwrite") \
    .save("/delta/events")

# Create managed Delta table
events.write.format("delta") \
    .saveAsTable("events_table")

SQL – Create Delta Table
CREATE TABLE events_delta
USING DELTA
AS SELECT * FROM events_table;

###Schema Enforcement Test
try:
    wrong_schema = spark.createDataFrame(
        [("a", "b", "c")],
        ["x", "y", "z"]
    )
    wrong_schema.write.format("delta") \
        .mode("append") \
        .save("/delta/events")
except Exception as e:
    print(f"Schema enforcement error: {e}")
🎯 Key Takeaways

Delta Lake enables reliable data pipelines

ACID transactions are critical for production systems

Schema enforcement improves data quality

Delta tables are safer than raw Parquet files

🔧 Tools & Technologies

Databricks
Apache Spark
Delta Lake
PySpark
Spark SQL
