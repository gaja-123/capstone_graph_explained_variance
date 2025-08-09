import streamlit as st
import plotly.graph_objects as go

# Data
labels = ['KNN', 'Decision Tree', 'XGBoost', 'Random Forest', 'CatBoost', 'LightGBM']
before_ev = [0.6177, 0.4146, 0.6839, 0.6320, 0.6863, 0.6831]
after_ev = [0.6463, 0.6654, 0.6782, 0.6802, 0.6854, 0.6868]

# Create figure
fig = go.Figure()

# Before tuning
fig.add_trace(go.Bar(
    x=labels,
    y=before_ev,
    name='Explained Variance (Before Tuning)',
    marker_color='rgba(54, 162, 235, 0.6)'
))

# After tuning
fig.add_trace(go.Bar(
    x=labels,
    y=after_ev,
    name='Explained Variance (After Tuning)',
    marker_color='rgba(75, 192, 192, 0.6)'
))

# Layout
fig.update_layout(
    title='Explained Variance Comparison: Before vs. After Tuning',
    xaxis_title='Models (Sorted by After-Tuning Explained Variance)',
    yaxis_title='Explained Variance',
    yaxis=dict(range=[0, 0.8]),
    barmode='group',
    legend=dict(x=0.8, y=1.1)
)

# Streamlit display
st.title("Explained Variance Dashboard")
st.plotly_chart(fig, use_container_width=True)
