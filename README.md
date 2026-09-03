# E-Commerce Data Pipeline & Machine Learning Architecture

A complete data engineering and predictive machine learning system built across 4 development tiers.

## 🚀 Project Tiers

### Tier 1: Relational Data Ingestion & SQL Architecture
- **ETL Ingestion:** Data cleaning routines (`scripts/clean_and_load.py`).
- **Database Schema:** Structured relational schemas (`sql/create_tables.sql`).
- **Analytical SQL:** Key performance query routines (`sql/analytical_queries.sql`).

### Tier 2: Visual Analytics & BI Reporting
- Automated statistical charts using `seaborn` and `matplotlib` (`scripts/generate_charts.py`).
- Automatic visual exports saved directly to `outputs/`.

### Tier 3: Machine Learning & Customer Churn Modeling
- Target feature definition for churn recency (`days_since_last_purchase > 60`).
- Random Forest Classifier model training (`scripts/train_model.py`).

### Tier 4: Pipeline Automation & Productionization
- End-to-end Scikit-Learn `Pipeline` with feature scaling (`scripts/pipeline_production.py`).
- Model artifact serialization with `joblib` (`models/churn_pipeline_v1.pkl`).
- Automated batch scoring and risk exports (`outputs/batch_churn_predictions.csv`).

---

## 🛠️ Execution Instructions

1. **Install Dependencies:**
   ```bash
   pip install pandas numpy scikit-learn seaborn matplotlib joblib