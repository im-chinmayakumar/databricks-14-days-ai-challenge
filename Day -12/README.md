# Day 12 (20/01/26) – MLflow Basics 🤖  
## Phase 4: AI & ML

## 📌 Overview
Day 12 introduced **MLflow**, a platform for managing the end-to-end
machine learning lifecycle. The focus was on **experiment tracking,
model logging, and comparison of runs**.

---

## 📘 What I Learned

- **MLflow Components**  
  Explored MLflow Tracking, Models, and the Model Registry.

- **Experiment Tracking**  
  Logged parameters, metrics, and artifacts for reproducibility.

- **Model Logging**  
  Saved trained models using MLflow for reuse and deployment.

- **MLflow UI**  
  Compared multiple runs to evaluate model performance.

---

## 🛠️ Hands-On Tasks

1. Trained a simple regression model  
2. Logged parameters and metrics using MLflow  
3. Logged trained models  
4. Compared runs in the MLflow UI  

---

## 🧪 Practice & Implementation

### Model Training & MLflow Tracking
```python
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Prepare data
df = spark.table("gold.products").toPandas()

X = df[["views", "cart_adds"]]
y = df["purchases"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

# MLflow experiment
with mlflow.start_run(run_name="linear_regression_v1"):
    # Log parameters
    mlflow.log_param("model_type", "LinearRegression")
    mlflow.log_param("test_size", 0.2)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate
    score = model.score(X_test, y_test)
    mlflow.log_metric("r2_score", score)

    # Log model
    mlflow.sklearn.log_model(model, "model")

print(f"R² Score: {score:.4f}")


