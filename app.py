import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    return pd.read_csv('clustered_customers.csv')

df = load_data()

df['Cluster'] = df['Cluster'].astype(str)

custom_colors = {
    '0': 'blue',
    '1': 'red',
    '2': 'gold',
    '3': 'green'
}

st.title("Customer Segmentation Visualizations")

# 1. 3D Scatter Plot (MonetaryValue vs Frequency vs Recency)
fig1 = px.scatter_3d(
    df,
    x='MonetaryValue', 
    y='Frequency', 
    z='Recency', 
    color='Cluster',  # Use Cluster column
    title='3D RFM with 4 Segments',
    labels={'MonetaryValue': 'Monetary Value', 'Frequency': 'Frequency', 'Recency': 'Recency'},
    opacity=0.7,
    color_discrete_map=custom_colors
)
st.plotly_chart(fig1)

# 2. 2D Scatter Plot (MonetaryValue vs Frequency)
fig2 = px.scatter(
    df,
    x='MonetaryValue',
    y='Frequency',
    color='Cluster',
    title='Monetary Value vs Frequency with 4 segments',
    labels={'MonetaryValue': 'Monetary Value', 'Frequency': 'Frequency'},
    opacity=0.7,
    hover_data=['Recency'],
    color_discrete_map=custom_colors
)
fig2.update_traces(marker=dict(size=8, line=dict(width=0.5, color='DarkSlateGrey')))
st.plotly_chart(fig2)

# 3. 2D Scatter Plot (MonetaryValue vs Recency)
fig3 = px.scatter(
    df,
    x='MonetaryValue',
    y='Recency',
    color='Cluster',
    title='Monetary Value vs Recency with 4 segments',
    labels={'MonetaryValue': 'Monetary Value', 'Recency': 'Recency'},
    opacity=0.7,
    hover_data=['Frequency'],
    color_discrete_map=custom_colors
)
fig3.update_traces(marker=dict(size=8, line=dict(width=0.5, color='DarkSlateGrey')))
st.plotly_chart(fig3)
