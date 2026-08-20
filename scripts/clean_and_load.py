from sqlalchemy import create_engine

# For PostgreSQL
# Syntax: postgresql://<username>:<password>@<host>:<port>/<database>
db_url = "postgresql://postgres:yourpassword@localhost:5432/ecommerce_db"

# For MySQL (requires: pip install pymysql)
# Syntax: mysql+pymysql://<username>:<password>@<host>:<port>/<database>
# db_url = "mysql+pymysql://root:yourpassword@localhost:3306/ecommerce_db"

# Create the engine connection
engine = create_engine(db_url)

# Test the connection
with engine.connect() as connection:
    print("Successfully connected to the SQL database!")

print("hello world")