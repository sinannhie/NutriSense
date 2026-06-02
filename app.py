
import streamlit as st

st.set_page_config(
    page_title="NutriSense",
    page_icon="🥗",
    layout="wide"
)

st.title("🥗 NutriSense")

st.subheader(
    "AI-Powered Obesity Prediction & Nutrition Analytics Platform"
)

st.info(
    """
    Predict obesity risk, analyze nutrition metrics,
    and receive personalized health recommendations.
    """
)

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

st.header("📌 Platform Modules")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Prediction", "XGBoost")

with col2:
    st.metric("Nutrition", "BMI • BMR • TDEE")

with col3:
    st.metric("Explainability", "SHAP")

with col4:
    st.metric("Insights", "Personalized")

st.markdown("---")

st.caption(
    "NutriSense v1.0 • Developed by Muhammed Sinan M"
)
