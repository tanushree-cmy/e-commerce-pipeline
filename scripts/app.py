import os
import subprocess
import sys
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

# Resolve project paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "ecommerce.db")
SCRIPT_PATH = os.path.join(BASE_DIR, "scripts", "clean_and_load.py")

def init_db():
    subprocess.run([sys.executable, SCRIPT_PATH], check=True)

# Auto-generate DB if missing on app boot
if not os.path.exists(DB_PATH):
    init_db()

st.title("🛒 E-Commerce Inventory & Pipeline Dashboard")
page = st.sidebar.radio("Navigation", ["Overview", "Database Tables", "Run Production Pipeline"])

if page == "Overview":
    st.subheader("Pipeline Overview")
    st.write("Visualizing database operations directly in the browser.")
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
        try:
            init_db()
            st.success("Pipeline executed successfully! All tables updated.")
        except Exception as e:
            st.error(f"Pipeline execution failed: {e}")

elif page == "Database Tables":
    st.subheader("Live Database Records")
    engine = create_engine(f"sqlite:///{DB_PATH}")
    
    table_name = st.selectbox("Select Table", ["users", "products", "orders"])
    
    try:
        df = pd.read_sql(f"SELECT * FROM {table_name}", con=engine)
        st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.error(f"Could not load table: {e}")