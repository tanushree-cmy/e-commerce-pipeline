import os
import subprocess
import sys
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

# Database setup
DB_FILE = "ecommerce.db"
engine = create_engine(f"sqlite:///{DB_FILE}")

# Automatically create tables if the database does not exist
if not os.path.exists(DB_FILE):
    subprocess.run([sys.executable, "scripts/clean_and_load.py"])

# Streamlit UI Navigation
st.title("🛒 E-Commerce Inventory & Pipeline Dashboard")
page = st.sidebar.radio("Navigation", ["Overview", "Database Tables", "Run Production Pipeline"])

if page == "Overview":
    st.subheader("Pipeline Overview")
    st.write("Visualizing Tier-1 through Tier-4 database operations directly in the browser.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.caption("Database Engine")
        st.markdown("### SQLite / SQLAlchemy")
    with col2:
        st.caption("Status")
        st.markdown("### Active & Connected")

elif page == "Run Production Pipeline":
    st.subheader("Pipeline Controls")
    if st.button("Execute Pipeline Batch"):
        st.info("Running pipeline scripts...")
        # Use sys.executable to ensure subprocess runs in the current Python runtime
        result = subprocess.run([sys.executable, "scripts/clean_and_load.py"], capture_output=True, text=True)
        if result.returncode == 0:
            st.success("Pipeline executed successfully!")
        else:
            st.error(f"Pipeline execution failed: {result.stderr}")

elif page == "Database Tables":
    st.subheader("Live Database Records")
    
    table_name = st.selectbox("Select Table", ["users", "products", "orders"])
    
    try:
        df = pd.read_sql(f"SELECT * FROM {table_name}", con=engine)
        st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.error(f"Could not load table: {e}")