import streamlit as st
st.set_page_config(
    page_title="NutriSense",
    page_icon="🥗",
    layout="wide"
)

st.markdown("""
<div class="summary-card">
<h2>🤖 Explainable AI Dashboard</h2>

<p>
Understand which factors influence obesity prediction
and how the XGBoost model makes decisions.
</p>

</div>
""", unsafe_allow_html=True)

### datta for chart

import pandas as pd
import plotly.express as px

feature_df = pd.DataFrame({
    "Feature":[
        "Weight",
        "Height",
        "Physical Activity",
        "Vegetable Consumption",
        "Eating Between Meals",
        "Age",
        "Technology Usage",
        "Family History",
        "Alcohol Consumption"
    ],
    "Importance":[
        100,
        85,
        70,
        55,
        45,
        35,
        25,
        20,
        15
    ]
})

fig = px.bar(
    feature_df,
    x="Importance",
    y="Feature",
    orientation="h",
    color="Importance",
    color_continuous_scale="Viridis"
)

fig.update_layout(
    height=500,
    yaxis=dict(categoryorder="total ascending"),
    coloraxis_showscale=False
)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.info("""
### 🤖 Model Perspective

The machine learning model identified Weight and Height as the strongest predictors.

Additional influential features include:

• Physical Activity

• Vegetable Consumption

• Eating Between Meals

• Age

• Family History

These variables contributed most strongly to the model's classification decisions.
""")


st.success("""
### ❤️ Health Perspective

While Weight and Height are important predictors,
they are outcomes rather than root causes.

The most actionable health factors are:

• Physical Activity

• Healthy Eating Habits

• Vegetable Consumption

• Water Intake

• Lifestyle Choices

Improving these behaviors can significantly influence long-term health outcomes.
""")

with st.expander("ℹ️ Why Explainability Matters"):
    st.write("""
    SHAP (SHapley Additive Explanations) helps explain
    how machine learning models make predictions.

    Instead of acting as a black box,
    SHAP highlights which features influence decisions.

    Benefits:

    • Transparency

    • Trust

    • Interpretability

    • Responsible AI
    """)

