# Databricks notebook source
ecommerce_df = spark.read.option("header", True).option("inferSchema", True).csv(
    "/Volumes/workspace/ecommerce/ecommerce_data"
)
ecommerce_df.write.format("delta").mode("overwrite").save(
    "/Volumes/workspace/ecommerce/ecommerce_data_delta"
)

# COMMAND ----------

spark.read.format("delta").load("/Volumes/workspace/ecommerce/ecommerce_data_delta").display()

# COMMAND ----------

# MAGIC %sql
# MAGIC USE CATALOG workspace;
# MAGIC USE SCHEMA ecommerce;

# COMMAND ----------

# MAGIC %sql CREATE TABLE ecommerce_event_sql AS SELECT * FROM delta.`/Volumes/workspace/ecommerce/ecommerce_data_delta`;

# COMMAND ----------

# MAGIC %sql SELECT COUNT(*) FROM ecommerce_event_sql;

# COMMAND ----------

# MAGIC %sql DESCRIBE ecommerce_event_sql;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Try intersecting wrong type
# MAGIC INSERT INTO ecommerce_event_sql
# MAGIC VALUES (
# MAGIC   'not_a_timestamp',
# MAGIC   'purchased',
# MAGIC   1234,
# MAGIC   765789,
# MAGIC   'electronics.smartphone',
# MAGIC   'Realme',
# MAGIC   'free',
# MAGIC   999,
# MAGIC   'abc-session'
# MAGIC );

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) FROM ecommerce_event_sql;