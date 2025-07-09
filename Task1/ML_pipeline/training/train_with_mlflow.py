import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Set MLflow experiment
mlflow.set_experiment("Heart Disease Classification")

# Load dataset
df = pd.read_csv("heart.csv")
print(df.head())
print("\nMissing values:\n", df.isnull().sum())

# Encode categorical features
df_encoded = pd.get_dummies(df, drop_first=True)

# Split features and target
X = df_encoded.drop("HeartDisease", axis=1)
y = df_encoded["HeartDisease"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Start MLflow tracking
with mlflow.start_run():
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)

    acc = accuracy_score(y_test, y_pred)
    print("✅ Accuracy:", acc)
    print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))

    # Confusion matrix plot (optional, not logged)
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

    # Log parameters and metrics
    mlflow.log_param("n_estimators", 100)
    mlflow.log_metric("accuracy", acc)

    # Log model and scaler
    mlflow.sklearn.log_model(model, "random_forest_model")

    with open("heart_scaler.pkl", "wb") as f:
        pickle.dump(scaler, f)
    mlflow.log_artifact("heart_scaler.pkl")

    print("✅ MLflow logging complete.")
