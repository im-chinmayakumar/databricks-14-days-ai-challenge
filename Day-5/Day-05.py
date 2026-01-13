# Databricks notebook source
from delta.tables import DeltaTable
from pyspark.sql import functions as F


# COMMAND ----------

spark.read.format("delta").load("/Volumes/workspace/ecommerce/ecommerce_data_delta").display(5)

# COMMAND ----------

updates = spark.createDataFrame([
    ("u101", "2024-01-05 10:00:00", "purchase", 1200),
    ("u202", "2024-01-05 11:00:00", "click", 0),
    ("u303", "2024-01-05 12:00:00", "add_to_cart", 500)
], ["user_session", "event_time", "event_type", "amount"])

updates.show()


# COMMAND ----------

from delta.tables import DeltaTable

delta_path = "/Volumes/workspace/ecommerce/ecommerce_data_delta"

deltaTable = DeltaTable.forPath(spark, delta_path)

updates.display()


# COMMAND ----------

deltaTable = DeltaTable.forPath(
    spark,
    "/Volumes/workspace/ecommerce/ecommerce_data_delta"
)


# COMMAND ----------

updates = spark.createDataFrame(
    [
        ("u101", "2024-01-06 10:00:00", "purchase", 1500),
        ("u202", "2024-01-06 11:00:00", "click", 0)
    ],
    ["user_session", "event_time", "event_type", "amount"]
)


# COMMAND ----------

deltaTable.alias("t").merge(
    updates.alias("s"),
    "t.user_session = s.user_session AND t.event_time = s.event_time"
).whenMatchedUpdate(
    set={
        "event_type": "s.event_type",
        "price": "s.amount" 
    }
).whenNotMatchedInsert(
    values={
        "user_session": "s.user_session",
        "event_time": "s.event_time",
        "event_type": "s.event_type",
        "price": "s.amount"   
    }
).execute()


# COMMAND ----------

spark.sql("""
DESCRIBE HISTORY delta.`/Volumes/workspace/ecommerce/ecommerce_data_delta`
""").display()


# COMMAND ----------

spark.read.format("delta") \
  .load("/Volumes/workspace/ecommerce/ecommerce_data_delta") \
  .filter("user_session in ('u101','u202')") \
  .display()
