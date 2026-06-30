# Created with GrishteSync
# https://suryasticsai.github.io/GrishteSync
# Suryasticsai | suryasticsai@gmail.com
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import snowflake.connector

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

# Create a Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div(children=[
    html.H1(children='KPI Dashboard'),
    html.Img(src='https://i.ibb.co/RGmb4FKk/1781072041102.png'),
    dcc.Graph(id='revenue-graph'),
    dcc.Graph(id='churn-graph'),
    dcc.Interval(
        id='interval-component',
        interval=86400000, # refresh every 24 hours
        n_intervals=0
    )
])

# Define a callback to update the graphs
@app.callback(
    [Output('revenue-graph', 'figure'), Output('churn-graph', 'figure')],
    [Input('interval-component', 'n_intervals')]
)
def update_graphs(n):
    # Query Snowflake for revenue and churn metrics
    ctx = snowflake.connector.connect(
        user='YOUR_USERNAME',
        password='YOUR_PASSWORD',
        account='YOUR_ACCOUNT',
        warehouse='YOUR_WAREHOUSE',
        database='YOUR_DATABASE',
        schema='YOUR_SCHEMA'
    )
    cursor = ctx.cursor()
    cursor.execute("SELECT * FROM revenue_and_churn_metrics")
    results = cursor.fetchall()
    ctx.close()
    
    # Create a Pandas dataframe from the query results
df = pd.DataFrame(results)
    
    # Create figures for the graphs
    revenue_fig = px.line(df, x='date', y='revenue')
    churn_fig = px.line(df, x='date', y='churn')
    
    return revenue_fig, churn_fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

# Made with GrishteSync | Suryasticsai | suryasticsai@gmail.com