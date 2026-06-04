
import streamlit as st

st.set_page_config(
    page_title="NutriSense",
    page_icon="🥗",
    layout="wide"
)



st.markdown("""
<div style="
padding:40px;
border-radius:20px;
background:linear-gradient(
135deg,
#0f172a,
#1e293b
);
color:white;
">

<h1>🥗 NutriSense AI</h1>

<h3>
AI-Powered Obesity Prediction &
Nutrition Analytics Platform
</h3>

<p style="font-size:18px;">
Predict obesity risk, analyze health metrics,
and generate personalized nutrition reports
using Machine Learning and Explainable AI.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.header("🚀 What Would You Like To Do?")

col1, col2 = st.columns(2)

with col1:
    st.success(
        """
        ### 🤖 Obesity Prediction

        Predict obesity levels using machine learning
        and receive personalized health insights.
        """
    )

    st.page_link(
        "pages/1_🤖_Obesity_Prediction.py",
        label="Start Prediction",
        icon="🤖"
    )

with col2:
    st.success(
        """
        ### 🔥 Nutrition Analytics

        Explore BMI, BMR, TDEE, calorie goals,
        protein targets and hydration goals.
        """
    )

    st.page_link(
        "pages/2_🔥_Nutrition_Analytics.py",
        label="Open Nutrition Analytics",
        icon="🔥"
    )

st.markdown("---")

st.header("✨ Key Features")

col1,col2,col3 = st.columns(3)

with col1:
    st.info("""
### 🤖 AI Prediction

Predict obesity levels using
an XGBoost machine learning model.
""")

with col2:
    st.info("""
### 📊 Nutrition Analytics

BMI, BMR, TDEE,
calorie and hydration targets.
""")

with col3:
    st.info("""
### 📄 PDF Reports

Generate downloadable
health assessment reports.
""")

st.header("📊 Platform Overview")

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric(
        "🎯 Accuracy",
        "96.65%"
    )

with col2:
    st.metric(
        "📂 Dataset",
        "2111+"
    )

with col3:
    st.metric(
        "🏷 Classes",
        "7"
    )

with col4:
    st.metric(
        "🧠 Explainability",
        "SHAP"
    )

st.header("🏆 Model Performance")

col1,col2 = st.columns(2)

with col1:
    st.metric("Accuracy","96.65%")

with col2:
    st.metric("Macro F1","0.97")


st.markdown("---")

st.caption(
"""
NutriSense AI v1.0 |
Machine Learning • Nutrition Analytics • Explainable AI

Developed by Muhammed Sinan M
"""
)

