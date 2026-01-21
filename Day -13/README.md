# Day 13 (21/01/26) – Model Comparison & Feature Engineering 🤖  
## Phase 4: AI & ML

## 📌 Overview
Day 13 focused on **training, comparing, and selecting machine learning models**
using **MLflow and Spark ML Pipelines**.  
The objective was to understand how **experimentation, feature engineering,
and evaluation** work together in real ML workflows.

---

## 📘 What I Learned

- **Training Multiple Models**  
  Trained and evaluated multiple models to compare performance objectively.

- **Hyperparameter Tuning (Basics)**  
  Explored how model parameters impact performance.

- **Feature Importance & Engineering**  
  Used meaningful features to improve model quality.

- **Spark ML Pipelines**  
  Built scalable pipelines to standardize feature preparation and model training.

---

## 🛠️ Hands-On Tasks

1. Trained three different ML models  
2. Compared evaluation metrics using MLflow  
3. Logged parameters, metrics, and models  
4. Built a Spark ML pipeline  
5. Selected the best-performing model  

---

## 🧪 Practice & Implementation

### Train & Compare Multiple Models (MLflow)
```python
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

models = {
    "linear": LinearRegression(),
    "decision_tree": DecisionTreeRegressor(max_depth=5),
    "random_forest": RandomForestRegressor(n_estimators=100)
}

for name, model in models.items():
    with mlflow.start_run(run_name=f"{name}_model"):
        mlflow.log_param("model_type", name)

        model.fit(X_train, y_train)
        score = model.score(X_test, y_test)

        mlflow.log_metric("r2_score", score)
        mlflow.sklearn.log_model(model, "model")

        print(f"{name}: R² = {score:.4f}")
Spark ML Pipeline
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression as SparkLR

assembler = VectorAssembler(
    inputCols=["views", "cart_adds"],
    outputCol="features"
)

lr = SparkLR(
    featuresCol="features",
    labelCol="purchases"
)

pipeline = Pipeline(stages=[assembler, lr])

spark_df = spark.table("gold.products")
train, test = spark_df.randomSplit([0.8, 0.2])

model = pipeline.fit(train)

🎯 Key Takeaways

Comparing multiple models leads to better decision-making

MLflow simplifies experiment tracking and evaluation

Feature engineering strongly impacts model performance

Spark ML Pipelines enable scalable and reusable ML workflows
