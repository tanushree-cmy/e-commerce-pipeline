import os
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

def run_production_pipeline():
    print("--- [Tier 4] Initiating Production ML Pipeline Execution ---")
    
    # Create outputs directory for models if it doesn't exist
    os.makedirs('models', exist_ok=True)
    os.makedirs('outputs', exist_ok=True)
    
    # 1. Feature Ingestion & Dataset Construction
    np.random.seed(42)
    n_customers = 500
    df = pd.DataFrame({
        'total_orders': np.random.randint(1, 20, size=n_customers),
        'avg_order_value': np.random.uniform(20.0, 500.0, size=n_customers),
        'days_since_last_purchase': np.random.randint(1, 150, size=n_customers),
        'total_spent': np.random.uniform(100.0, 5000.0, size=n_customers)
    })
    df['is_churned'] = np.where(df['days_since_last_purchase'] > 60, 1, 0)
    
    X = df.drop(columns=['is_churned'])
    y = df['is_churned']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 2. Build Scikit-Learn Automated Production Pipeline
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42))
    ])
    
    # 3. Train Pipeline
    pipeline.fit(X_train, y_train)
    
    # 4. Evaluate Metrics
    preds = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, preds)
    f1 = f1_score(y_test, preds)
    
    print(f"Pipeline Accuracy: {accuracy:.4f}")
    print(f"Pipeline F1-Score: {f1:.4f}")
    
    # 5. Model Serialization (Save Artifact for Deployment)
    model_path = 'models/churn_pipeline_v1.pkl'
    joblib.dump(pipeline, model_path)
    print(f"SUCCESS: Production Model Pipeline saved to '{model_path}'")
    
    # 6. Automated Batch Inference (Generate Risk Score File)
    df['churn_prediction'] = pipeline.predict(X)
    df['churn_probability'] = pipeline.predict_proba(X)[:, 1]
    
    output_path = 'outputs/batch_churn_predictions.csv'
    df.to_csv(output_path, index=False)
    print(f"SUCCESS: Batch Inference predictions written to '{output_path}'")

if __name__ == "__main__":
    run_production_pipeline()

