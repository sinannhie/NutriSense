import streamlit as st
st.set_page_config(
    page_title="NutriSense",
    page_icon="🥗",
    layout="wide"
)
st.header("🤖 Model Perspective")

st.write("""
The SHAP analysis identified the following features as having the strongest influence on obesity prediction:
""")

st.markdown("""
### Top Features Identified by SHAP

🥇 Weight

🥈 Height

🥉 Physical Activity (FAF)

4️⃣ Vegetable Consumption (FCVC)

5️⃣ Eating Between Meals (CAEC)

6️⃣ Age

7️⃣ Technology Usage (TUE)

8️⃣ Family History of Overweight

9️⃣ Alcohol Consumption (CALC)
""")

st.header("❤️ Health Perspective")

st.success("""
While Weight and Height are the strongest statistical predictors, they are not the root causes of obesity.

From a health and lifestyle perspective, the most actionable factors include:

• Physical Activity
• Eating Habits
• Vegetable Consumption
• Water Intake
• Family History Awareness
• Healthy Lifestyle Choices

These are the factors individuals can actively improve to support long-term health outcomes.
""")


st.header("🎯 Why Explainability Matters")

st.write("""
Traditional machine learning models often act as 'black boxes'.

SHAP helps make predictions transparent by identifying which features contribute most to the model's decisions.

This improves:

• Trust
• Transparency
• Interpretability
• Responsible AI Practices
""")