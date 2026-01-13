# Day 5 – Delta Lake Advanced 🚀  
## Phase 2: Data Engineering

## 📌 Overview
Day 5 marks the beginning of **Phase 2: Data Engineering**, with a deep dive into **advanced Delta Lake features**.  
The focus was on building **production-ready, optimized, and maintainable data pipelines** using Delta Lake.

---

## 📘 What I Learned

- **Delta Lake Time Travel**  
  Learned how to query historical versions of data using version numbers and timestamps for debugging and audits.

- **MERGE Operations (Upserts)**  
  Implemented incremental data updates using MERGE to handle inserts and updates atomically.

- **OPTIMIZE & ZORDER**  
  Improved query performance by compacting small files and organizing data for efficient access.

- **VACUUM**  
  Removed obsolete data files to manage storage efficiently while maintaining required data retention.

---

## 🛠️ Hands-On Tasks

1. Implemented incremental MERGE logic for Delta tables  
2. Queried historical data using Delta time travel  
3. Optimized Delta tables using OPTIMIZE and ZORDER  
4. Cleaned up old files using VACUUM  

---

## 🧪 Practice & Implementation

### Incremental MERGE (Upserts)
```python
from delta.tables import DeltaTable

deltaTable = DeltaTable.forPath(spark, "/delta/events")
updates = spark.read.csv(
    "/path/to/new_data.csv",
    header=True,
    inferSchema=True
)
---
### Delta Time Travel
```python
---
deltaTable.alias("t").merge(
    updates.alias("s"),
    "t.user_session = s.user_session AND t.event_time = s.event_time"
).whenMatchedUpdateAll() \
 .whenNotMatchedInsertAll() \
 .execute()

## Optimization & Cleanup
