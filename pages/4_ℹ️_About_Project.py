import streamlit as st

st.set_page_config(
    page_title="About NutriSense",
    page_icon="ℹ️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
    <style>
        .main { max-width: 1200px; }
        
        /* Title styling */
        .title-section {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2.5rem;
            border-radius: 15px;
            color: white;
            margin-bottom: 2rem;
        }
        
        /* Feature cards */
        .feature-card {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 1.5rem;
            border-radius: 12px;
            border-left: 5px solid #667eea;
            margin-bottom: 1rem;
        }
        
        /* Stats section */
        .stat-box {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1.5rem;
            border-radius: 10px;
            color: white;
            text-align: center;
        }
        
        .stat-label { font-size: 0.9rem; opacity: 0.9; }
        .stat-value { font-size: 2rem; font-weight: bold; margin-top: 0.5rem; }
        
        /* Section headers */
        .section-header {
            font-size: 1.8rem;
            font-weight: 700;
            color: #1f1f1f;
            margin-top: 2rem;
            margin-bottom: 1.5rem;
            border-bottom: 3px solid #667eea;
            padding-bottom: 0.5rem;
        }
        
        /* Achievement items */
        .achievement-item {
            padding: 0.8rem;
            margin: 0.5rem 0;
            background: rgba(102, 126, 234, 0.1);
            border-left: 4px solid #667eea;
            border-radius: 5px;
        }
        
        /* Developer card */
        .developer-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem;
            border-radius: 15px;
            text-align: center;
            margin: 2rem 0;
        }
    </style>
""", unsafe_allow_html=True)

# =========================
# HERO SECTION
# =========================
st.markdown("""
    <div class="title-section">
        <h1 style="margin: 0; font-size: 2.5rem;">🎯 About NutriSense</h1>
        <p style="margin: 1rem 0 0 0; font-size: 1.1rem; opacity: 0.95;">
            AI-Powered Obesity Prediction & Nutrition Analytics Platform
        </p>
        <p style="margin: 0.8rem 0 0 0; font-size: 0.95rem; opacity: 0.85;">
            Combining Machine Learning, Health Analytics, and Nutrition Intelligence 
            to help users understand obesity risk factors and receive personalized health insights.
        </p>
    </div>
""", unsafe_allow_html=True)

# =========================
# PROJECT OVERVIEW
# =========================
st.markdown('<h2 class="section-header">📋 Project Overview</h2>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="medium")

with col1:
    st.markdown("""
    **What is NutriSense?**
    
    An intelligent health analytics platform that combines machine learning with nutrition science 
    to help users make informed dietary decisions.
    """)

with col2:
    st.markdown("""
    **Key Benefits:**
    
    🔍 Predict obesity risk levels with high accuracy  
    📊 Calculate personalized nutrition metrics  
    💡 Get actionable health recommendations  
    🎯 Track progress towards health goals
    """)

# =========================
# MODEL PERFORMANCE
# =========================
st.markdown('<h2 class="section-header">📈 Model Performance</h2>', unsafe_allow_html=True)

perf_col1, perf_col2, perf_col3, perf_col4 = st.columns(4, gap="large")

metrics_data = [
    ("Accuracy", "~96%", "🎯"),
    ("Algorithm", "XGBoost", "⚙️"),
    ("Classes", "7", "📊"),
    ("Features", "16", "🔍")
]

for col, (label, value, emoji) in zip([perf_col1, perf_col2, perf_col3, perf_col4], metrics_data):
    with col:
        st.markdown(f"""
        <div class="stat-box">
            <div style="font-size: 2rem;">{emoji}</div>
            <div class="stat-label">{label}</div>
            <div class="stat-value">{value}</div>
        </div>
        """, unsafe_allow_html=True)



# =========================
# DATASET
# =========================
st.markdown('<h2 class="section-header">📊 Dataset Information</h2>', unsafe_allow_html=True)

st.markdown("""
The model was trained using the Obesity Levels Dataset containing comprehensive demographic, 
dietary, and lifestyle information to predict obesity risk with high accuracy.
""")

col1, col2, col3 = st.columns(3, gap="medium")

dataset_features = {
    col1: {
        "title": "👤 Health Features",
        "items": ["Age", "Gender", "Height", "Weight"]
    },
    col2: {
        "title": "🏃 Lifestyle Features",
        "items": ["Physical Activity", "Transportation", "Smoking", "Alcohol Consumption"]
    },
    col3: {
        "title": "🍎 Dietary Features",
        "items": ["Vegetable Intake", "Water Intake", "Eating Habits", "Family History"]
    }
}

for col, data in dataset_features.items():
    with col:
        st.markdown(f"**{data['title']}**")
        for item in data['items']:
            st.markdown(f"<div class='achievement-item'>• {item}</div>", unsafe_allow_html=True)



# =========================
# FEATURES
# =========================
st.markdown('<h2 class="section-header">⚙️ Platform Features</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

core_features = [
    "✅ Obesity Level Prediction",
    "✅ BMI Calculator",
    "✅ BMR (Basal Metabolic Rate) Calculation",
    "✅ TDEE (Total Daily Energy Expenditure) Estimation",
    "✅ Personalized Health Recommendations"
]

analytics_features = [
    "✅ Nutrition Analytics Dashboard",
    "✅ Water Intake Tracking & Targets",
    "✅ Protein Goal Calculator",
    "✅ Session State Management",
    "✅ Multi-Page Architecture"
]

with col1:
    st.markdown("**🎯 Core Prediction Features**")
    for feature in core_features:
        st.markdown(f"<div class='achievement-item'>{feature}</div>", unsafe_allow_html=True)

with col2:
    st.markdown("**📊 Analytics & Tracking**")
    for feature in analytics_features:
        st.markdown(f"<div class='achievement-item'>{feature}</div>", unsafe_allow_html=True)



# =========================
# KEY ACHIEVEMENTS
# =========================
st.markdown('<h2 class="section-header">🏆 Key Achievements</h2>', unsafe_allow_html=True)

achievements = [
    ("🎯", "96% Prediction Accuracy", "Leveraging XGBoost for high-precision obesity classification"),
    ("📊", "SHAP Explainability Analysis", "Complete model interpretability and feature importance analysis"),
    ("🔥", "Nutrition Analytics Dashboard", "Integrated tracking system with real-time calculations"),
    ("🔄", "Session State Communication", "Seamless data flow between application pages"),
    ("📱", "Professional UI/UX", "Multi-page Streamlit application with responsive design")
]

for emoji, title, description in achievements:
    st.markdown(f"""
    <div class='achievement-item' style='padding: 1rem; margin: 0.8rem 0;'>
        <span style='font-size: 1.3rem;'>{emoji}</span> 
        <strong>{title}</strong>
        <br/>
        <span style='opacity: 0.8; font-size: 0.9rem;'>{description}</span>
    </div>
    """, unsafe_allow_html=True)



# =========================
# FUTURE ROADMAP
# =========================
st.markdown('<h2 class="section-header">🚀 Future Roadmap</h2>', unsafe_allow_html=True)

roadmap_items = [
    ("📊", "Interactive SHAP Dashboard", "Advanced model explainability visualization"),
    ("🍽️", "Smart Food Recommendation System", "AI-powered personalized meal suggestions"),
    ("📈", "Advanced Health Analytics", "Trend analysis and predictive insights"),
    ("🤖", "AI Health Assistant", "Conversational AI for health guidance"),
    ("📄", "PDF Health Reports", "Generate personalized health summary reports"),
    ("📅", "Weekly Progress Tracking", "Monitor health metrics over time"),
    ("👤", "User Profiles", "Personalized user accounts and preferences"),
    ("☁️", "Cloud Deployment", "Scale to production environment")
]

col1, col2 = st.columns(2, gap="medium")

for i, (emoji, title, description) in enumerate(roadmap_items):
    col = col1 if i % 2 == 0 else col2
    with col:
        st.markdown(f"""
        <div class='achievement-item' style='padding: 1rem;'>
            <strong>{emoji} {title}</strong>
            <br/>
            <span style='opacity: 0.8; font-size: 0.9rem;'>{description}</span>
        </div>
        """, unsafe_allow_html=True)



# =========================
# DEVELOPER
# =========================
st.markdown('<h2 class="section-header">👨‍💻 Developer</h2>', unsafe_allow_html=True)

st.markdown("""
    <div class="developer-card">
        <h3 style="margin: 0; font-size: 1.8rem;">Muhammed Sinan M</h3>
        <p style="margin: 0.5rem 0; font-size: 1rem; opacity: 0.95;">
            Data Science & Machine Learning Developer
        </p>
        <hr style="border: 1px solid rgba(255,255,255,0.3); margin: 1rem 0;">
        <div style="text-align: left; margin: 1rem 0;">
            <p style="margin: 0.3rem 0;">🏆 Microsoft Data Science Certified</p>
            <p style="margin: 0.3rem 0;">🎓 BCA Graduate</p>
            <p style="margin: 0.3rem 0;">🏢 Cyber Square Calicut</p>
        </div>
        <p style="margin: 1rem 0 0 0; font-size: 0.95rem; opacity: 0.9;">
            <strong>NutriSense v1.0</strong>
        </p>
    </div>
""", unsafe_allow_html=True)

# =========================
# GITHUB & FOOTER
# =========================
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.link_button(
        "🔗 View Source Code on GitHub",
        "https://github.com/sinannhie/NutriSense.git",
        use_container_width=True
    )

st.markdown("---")

footer_col1, footer_col2, footer_col3 = st.columns(3)

with footer_col2:
    st.markdown(
        "<p style='text-align: center; color: #666; font-size: 0.9rem;'>"
        "Developed by <strong>Muhammed Sinan M</strong><br>"
        "NutriSense v1.0 © 2024<br>"
        "<span style='font-size: 0.85rem;'>AI-Powered Health Analytics Platform</span>"
        "</p>",
        unsafe_allow_html=True
    )
