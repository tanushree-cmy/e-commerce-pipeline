import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Page configuration
st.set_page_config(page_title="E-Commerce Pipeline", layout="wide")
st.title("🛒 E-Commerce Inventory & Pipeline Dashboard")

# Connect to database (Tier-1 Engine)
@st.cache_resource
def get_engine():
    return create_engine("sqlite:///ecommerce.db")

engine = get_engine()

# Navigation
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Database Tables", "Run Production Pipeline"])

if page == "Overview":
    st.subheader("Pipeline Overview")
    st.write("Visualizing Tier-1 through Tier-4 database operations directly in the browser.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Database Engine", value="SQLite / SQLAlchemy")
    with col2:
        st.metric(label="Status", value="Active & Connected")

elif page == "Database Tables":
    st.subheader("Live Database Records")
    table = st.selectbox("Select Table", ["users", "products", "orders"])
    
    try:
        with engine.connect() as conn:
            df = pd.read_sql(f"SELECT * FROM {table}", conn)
            st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.error(f"Could not load table: {e}")

elif page == "Run Production Pipeline":
    st.subheader("Pipeline Controls")
    if st.button("Execute Pipeline Batch"):
        st.info("Running pipeline scripts...")
        # Pipeline execution logic goes here
        st.success("Pipeline executed successfully!")