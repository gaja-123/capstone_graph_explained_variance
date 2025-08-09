import streamlit as st
import plotly.graph_objects as go

# Models with tuning
labels_tuned = ['KNN', 'Decision Tree', 'XGBoost', 'Random Forest', 'CatBoost', 'LightGBM']
before_ev_tuned = [0.6177, 0.4146, 0.6839, 0.6320, 0.6863, 0.6831]
after_ev_tuned = [0.6463, 0.6654, 0.6782, 0.6802, 0.6854, 0.6868]

# GLM (no tuning)
glm_label = ['GLM (No Tuning)']
glm_ev = [0.567]

# Dynamic y-axis max
y_max = max(max(before_ev_tuned + glm_ev), max(after_ev_tuned + glm_ev)) + 0.05

# Create figure
fig = go.Figure()

# Before tuning (tuned models)
fig.add_trace(go.Bar(
    x=labels_tuned,
    y=before_ev_tuned,
    name='Explained Variance (Before Tuning)',
    marker_color='#369FEF',
    text=[f"{v:.4f}" for v in before_ev_tuned],
    textposition='outside'
))

# After tuning (tuned models)
fig.add_trace(go.Bar(
    x=labels_tuned,
    y=after_ev_tuned,
    name='Explained Variance (After Tuning)',
    marker_color='#4BC0C0',
    text=[f"{v:.4f}" for v in after_ev_tuned],
    textposition='outside'
))

# GLM (no tuning)
fig.add_trace(go.Bar(
    x=glm_label,
    y=glm_ev,
    name='GLM (No Tuning)',
    marker_color='#B0BEC5',  # Neutral gray
    text=[f"{v:.4f}" for v in glm_ev],
    textposition='outside'
))

# Layout
fig.update_layout(
    title='Explained Variance Comparison: Before vs. After Tuning',
    xaxis_title='Models (GLM shown separately: No Tuning Applied)',
    yaxis_title='Explained Variance',
    yaxis=dict(range=[0, y_max]),
    barmode='group',
    legend=dict(x=0.75, y=1.1),
    margin=dict(t=80, b=40),
    height=500
)

# Streamlit display
st.set_page_config(page_title="Explained Variance Dashboard", layout="wide")
st.title("Explained Variance Dashboard")
st.plotly_chart(fig, use_container_width=True)
