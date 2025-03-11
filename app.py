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
    color='Cluster',
    title='3D RFM with 4 Segments',
    labels={'MonetaryValue': 'Monetary Value', 'Frequency': 'Frequency', 'Recency': 'Recency'},
    hover_data=['CustomerID'],  # Add any extra fields for hover
    opacity=0.8,
    color_discrete_map=custom_colors
)

fig1.update_traces(
    marker=dict(
        size=5,
        line=dict(width=0.5, color='DarkSlateGrey')
    )
)

fig1.update_layout(
    template='plotly_white',     # Switch to a white background
    scene=dict(
        aspectmode='cube',       # Make all axes scale the same
        xaxis=dict(range=[0, 20000]),
        yaxis=dict(range=[0, 25]),
        zaxis=dict(range=[0, 5000])
    ),
    scene_camera=dict(
        eye=dict(x=2, y=2, z=1)  # Initial camera view
    ),
    margin=dict(l=0, r=0, t=50, b=0),
    legend_title_text='Customer Cluster'
)

st.plotly_chart(fig1, use_container_width=True)

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
