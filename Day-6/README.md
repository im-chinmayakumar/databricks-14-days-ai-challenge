# Day 6 (14/01/26) – Medallion Architecture 🏅  
## Phase 2: Data Engineering

## 📌 Overview
Day 6 focused on implementing the **Medallion Architecture**, a best-practice data design pattern
used in modern data platforms to convert raw data into analytics-ready datasets.

---

## 📘 What I Learned

- **Bronze Layer (Raw)**  
  Stores raw ingested data with minimal transformations for traceability.

- **Silver Layer (Cleaned)**  
  Applies data cleaning, validation, deduplication, and feature engineering.

- **Gold Layer (Aggregated)**  
  Contains business-level aggregates optimized for reporting and analytics.

- **Incremental Processing Patterns**  
  Enables efficient data movement across layers without full reprocessing.

---

## 🛠️ Hands-On Tasks

1. Designed a 3-layer Medallion Architecture  
2. Built Bronze layer for raw ingestion  
3. Built Silver layer with data quality checks and enrichment  
4. Built Gold layer with business aggregates  

---

## 🧪 Practice & Implementation

## 🧪 Practice & Implementation

### 🥉 Bronze Layer – Raw Ingestion
```python
raw = spark.read.csv("/raw/events.csv", header=True, inferSchema=True)

raw.withColumn("ingestion_ts", F.current_timestamp()) \
   .write.format("delta") \
   .mode("overwrite") \
   .save("/delta/bronze/events")
---

### 🥈 Silver Layer – Cleaned & Validated Data
```python
bronze = spark.read.format("delta").load("/delta/bronze/events")

silver = bronze.filter(F.col("price") > 0) \
    .filter(F.col("price") < 10000) \
    .dropDuplicates(["user_session", "event_time"]) \
    .withColumn("event_date", F.to_date("event_time")) \
    .withColumn(
        "price_tier",
        F.when(F.col("price") < 10, "budget")
         .when(F.col("price") < 50, "mid")
         .otherwise("premium")
    )

silver.write.format("delta") \
    .mode("overwrite") \
    .save("/delta/silver/events")
---

### 🥇 Gold Layer – Business Aggregates
```python
silver = spark.read.format("delta").load("/delta/silver/events")

product_perf = silver.groupBy("product_id", "product_name") \
    .agg(
        F.countDistinct(
            F.when(F.col("event_type") == "view", "user_id")
        ).alias("views"),
        F.countDistinct(
            F.when(F.col("event_type") == "purchase", "user_id")
        ).alias("purchases"),
        F.sum(
            F.when(F.col("event_type") == "purchase", "price")
        ).alias("revenue")
    ) \
    .withColumn(
        "conversion_rate",
        (F.col("purchases") / F.col("views")) * 100
    )

product_perf.write.format("delta") \
    .mode("overwrite") \
    .save("/delta/gold/products")
---
