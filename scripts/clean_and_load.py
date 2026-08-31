from sqlalchemy import create_engine

# Use SQLite so you don't need a PostgreSQL server running
db_url = "sqlite:///ecommerce.db"

# Create the engine connection
engine = create_engine(db_url)

# Test the connection
with engine.connect() as connection:
    print("Successfully connected to the SQL database!")

print("hello world")
print("successfully")
print("connected")