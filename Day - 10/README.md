
---

# ✅ Day 10 GitHub README  
📁 **Path:** `Day-10/README.md`

```md
# Day 10 (18/01/26) – Performance Optimization ⚡  
## Phase 3: Advanced Analytics

## 📌 Overview
Day 10 focused on **performance optimization techniques** in Databricks.
The goal was to understand **how Spark executes queries** and how
**data layout, partitioning, and optimization** impact query performance.

---

## 📘 What I Learned

- **Query Execution Plans**  
  Used `explain()` to analyze logical, optimized, and physical query plans.

- **Partitioning Strategies**  
  Learned how partitioning large tables reduces data scanned and improves performance.

- **OPTIMIZE & ZORDER**  
  Applied file compaction and clustering to speed up frequent queries.

- **Caching Techniques**  
  Used caching for iterative workloads and measured execution time improvements.

---

## 🛠️ Hands-On Tasks

1. Analyzed Spark query execution plans  
2. Partitioned large Delta tables  
3. Applied OPTIMIZE and ZORDER on key columns  
4. Benchmarked query performance before and after optimization  

---

## 🧪 Practice & Implementation

### Analyze Query Execution Plan
```python
spark.sql("""
SELECT * 
FROM default.silver_movies 
WHERE studio = 'Warner Bros'
""").explain(True)

## Partition Large Table

CREATE OR REPLACE TABLE default.silver_movies_part
USING DELTA
PARTITIONED BY (release_year)
AS
SELECT * FROM default.silver_movies;


