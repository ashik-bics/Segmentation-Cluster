import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
@st.cache_data  # Cache data loading for efficiency
def load_data():
    df = pd.read_csv("clustered_customers.csv")
    return df

df = load_data()

# Ensure 'Cluster' column is treated as a string
df['Cluster'] = df['Cluster'].astype(str)

# Create 3D scatter plot
fig_3d = px.scatter_3d(
    df,
    x='MonetaryValue',
    y='Frequency',
    z='Recency',
    color='Cluster',
    title='3D Scatter Plot of Customer Data by Cluster',
    labels={'MonetaryValue': 'Monetary Value', 'Frequency': 'Frequency', 'Recency': 'Recency'},
    opacity=0.7
)

# Create 2D scatter plot
fig_2d = px.scatter(
    df,
    x='MonetaryValue',
    y='Frequency',
    color='Cluster',
    title='Customer Segments (2D Scatter Plot)',
    labels={'MonetaryValue': 'Monetary Value', 'Frequency': 'Frequency'},
    opacity=0.7,
    hover_data=['Recency'],  # Show Recency on hover
)

fig_2d.update_traces(marker=dict(size=8, line=dict(width=0.5, color='DarkSlateGrey')))

# Streamlit App Layout
st.title("Customer Segmentation Visualization")
st.plotly_chart(fig_3d)
st.plotly_chart(fig_2d)