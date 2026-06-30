# Created with GrishteSync
# https://suryasticsai.github.io/GrishteSync
# Suryasticsai | suryasticsai@gmail.com
import pandas as pd
import snowflake.connector

def get_revenue_and_churn_metrics():
    # Snowflake connection
    ctx = snowflake.connector.connect(
        user='YOUR_USERNAME',
        password='YOUR_PASSWORD',
        account='YOUR_ACCOUNT',
        warehouse='YOUR_WAREHOUSE',
        database='YOUR_DATABASE',
        schema='YOUR_SCHEMA'
    )
    
    # Query Snowflake for revenue and churn metrics
    cursor = ctx.cursor()
    cursor.execute("SELECT * FROM revenue_and_churn_metrics")
    results = cursor.fetchall()
    ctx.close()
    
    # Create a Pandas dataframe from the query results
df = pd.DataFrame(results)
    return df