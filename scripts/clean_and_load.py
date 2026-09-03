import os
import pandas as pd
from sqlalchemy import create_engine

# Set path relative to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "ecommerce.db")

engine = create_engine(f"sqlite:///{DB_PATH}")

# Sample Data Setup
users_df = pd.DataFrame({
    "user_id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"],
    "email": ["alice@example.com", "bob@example.com", "charlie@example.com"]
})

products_df = pd.DataFrame({
    "product_id": [101, 102, 103],
    "product_name": ["Laptop", "Mouse", "Keyboard"],
    "price": [999.99, 25.50, 45.00]
})

orders_df = pd.DataFrame({
    "order_id": [1001, 1002, 1003],
    "user_id": [1, 2, 1],
    "total_amount": [1025.49, 45.00, 999.99]
})

# Load Data into SQLite
users_df.to_sql("users", con=engine, if_exists="replace", index=False)
products_df.to_sql("products", con=engine, if_exists="replace", index=False)
orders_df.to_sql("orders", con=engine, if_exists="replace", index=False)

print("Database successfully populated with users, products, and orders!")