import os
import subprocess
import sys
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

# Ensure database exists on app start
DB_FILE = "ecommerce.db"
if not os.path.exists(DB_FILE):
    subprocess.run([sys.executable, "scripts/clean_and_load.py"])

# Streamlit App Navigation
page = st.sidebar.radio("Navigation", ["Overview", "Database Tables", "Run Production Pipeline"])

if page == "Run Production Pipeline":
    st.subheader("Pipeline Controls")
    if st.button("Execute Pipeline Batch"):
        st.info("Running pipeline scripts...")
        # Use sys.executable instead of hardcoded "python"
        subprocess.run([sys.executable, "scripts/clean_and_load.py"])
        st.success("Pipeline executed successfully!")

elif page == "Database Tables":
    st.subheader("Live Database Records")
    engine = create_engine(f"sqlite:///{DB_FILE}")
    
    table_name = st.selectbox("Select Table", ["users", "products", "orders"])
    
    if st.button("Fetch Data") or table_name:
        try:
            df = pd.read_sql(f"SELECT * FROM {table_name}", con=engine)
            st.dataframe(df)
        except Exception as e:
            st.error(f"Could not load table: {e}")