import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

def generate_dashboard():
    # 1. Setup in-memory SQLite database & load sample data
    conn = sqlite3.connect(':memory:')
    
    raw_data = {
        'user_id': [100, 100, 101, 102, 103, 104, 100],
        'category': ['Electronics', 'Apparel', 'Electronics', 'Groceries', 'Apparel', 'Electronics', 'Groceries'],
        'amount': [250.00, 45.50, 120.00, 85.20, 60.00, 310.00, 95.40],
        'purchase_date': ['2025-01-08', '2025-01-22', '2025-01-15', '2025-02-01', '2025-02-10', '2025-02-15', '2025-02-18']
    }
    df = pd.DataFrame(raw_data)
    df['purchase_date'] = pd.to_datetime(df['purchase_date'])
    df.to_sql('transactions', conn, index=False, if_exists='replace')

    # 2. SQL Aggregations for Charts
    query_category = """
    SELECT category, SUM(amount) AS total_revenue
    FROM transactions
    GROUP BY category
    ORDER BY total_revenue DESC;
    """
    df_category = pd.read_sql_query(query_category, conn)

    query_timeline = """
    SELECT purchase_date, SUM(amount) AS daily_revenue
    FROM transactions
    GROUP BY purchase_date
    ORDER BY purchase_date;
    """
    df_timeline = pd.read_sql_query(query_timeline, conn)
    conn.close()

    # 3. Render Seaborn Charts
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Bar Chart: Revenue by Category
    sns.barplot(data=df_category, x='category', y='total_revenue', ax=axes[0], palette='Blues_d')
    axes[0].set_title('Total Revenue by Category ($)', fontweight='bold')
    axes[0].set_ylabel('Revenue ($)')

    # Line Chart: Daily Revenue Trend
    sns.lineplot(data=df_timeline, x='purchase_date', y='daily_revenue', marker='o', ax=axes[1], color='#2b5c8f')
    axes[1].set_title('Daily Revenue Trend ($)', fontweight='bold')
    axes[1].set_ylabel('Revenue ($)')

    plt.tight_layout()
    plt.savefig('dashboard_output.png', dpi=300)
    print("SUCCESS: Saved dashboard chart to 'dashboard_output.png'!")
    plt.show()

if __name__ == "__main__":
    generate_dashboard()