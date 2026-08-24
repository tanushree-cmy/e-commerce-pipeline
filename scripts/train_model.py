import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def train_churn_predictor():
    print("--- [1/3] Engineering ML Features from E-Commerce Data ---")
    
    np.random.seed(42)
    n_customers = 300
    
    data = {
        'total_orders': np.random.randint(1, 15, size=n_customers),
        'avg_order_value': np.random.uniform(15.0, 350.0, size=n_customers),
        'days_since_last_purchase': np.random.randint(1, 120, size=n_customers),
        'total_spent': np.random.uniform(50.0, 2500.0, size=n_customers)
    }
    
    df = pd.DataFrame(data)
    
    # Target: 1 = Churned (no purchase in > 60 days), 0 = Active
    df['is_churned'] = np.where(df['days_since_last_purchase'] > 60, 1, 0)
    
    X = df[['total_orders', 'avg_order_value', 'days_since_last_purchase', 'total_spent']]
    y = df['is_churned']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("--- [2/3] Training Random Forest Classification Model ---")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    print("--- [3/3] Evaluating Predictive Model Performance ---")
    predictions = model.predict(X_test)
    
    print("\nModel Classification Report:")
    print(classification_report(y_test, predictions))

if __name__ == "__main__":
    train_churn_predictor()