
import streamlit as st

st.set_page_config(
    page_title="NutriSense",
    page_icon="🥗",
    layout="wide"
)

st.title("🔥 Nutrition Analytics")

bmi = st.session_state.get("bmi")
bmr = st.session_state.get("bmr")
weight = st.session_state.get("weight")
faf = st.session_state.get("faf")
ch2o = st.session_state.get("ch2o")


if bmi is None or bmr is None or weight is None or faf is None:
    st.warning("Please complete an obesity prediction first.")
    st.stop()

st.markdown("---")

# Activity Multiplier
if faf < 1:
    activity_multiplier = 1.2
    activity_level = "Sedentary"
elif faf < 2:
    activity_multiplier = 1.375
    activity_level = "Lightly Active"
elif faf < 3:
    activity_multiplier = 1.55
    activity_level = "Moderately Active"
else:
    activity_multiplier = 1.725
    activity_level = "Very Active"

# Calculations
tdee = bmr * activity_multiplier
maintenance_calories = tdee
fat_loss_calories = tdee - 500
muscle_gain_calories = tdee + 300
protein_target = weight * 1.8
water_target = weight * 0.035

# --- Section 1: Base Metrics ---
st.subheader("📊 Your Base Metrics")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("🔥 BMR", f"{bmr:.0f} kcal", help="Calories burned at complete rest")
with col2:
    st.metric("⚡ TDEE", f"{tdee:.0f} kcal", help="Total daily energy with activity")
with col3:
    st.metric("🏃 Activity Level", activity_level)

st.markdown("---")

# --- Section 2: Calorie Goals ---
st.subheader("🎯 Calorie Goals")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("⚖️ Maintenance", f"{maintenance_calories:.0f} kcal", delta="0 kcal")
with col2:
    st.metric("📉 Fat Loss", f"{fat_loss_calories:.0f} kcal", delta="-500 kcal")
with col3:
    st.metric("💪 Muscle Gain", f"{muscle_gain_calories:.0f} kcal", delta="+300 kcal")

st.markdown("---")

# --- Section 3: Nutrition Targets ---
st.subheader("🥗 Daily Nutrition Targets")
col1, col2 = st.columns(2)
with col1:
    st.metric("🍗 Protein Target", f"{protein_target:.0f} g/day", help="1.8g per kg bodyweight")
with col2:
    st.metric("💧 Water Target", f"{water_target:.1f} L/day", help="0.035L per kg bodyweight")

st.markdown("---")

# --- Summary ---
st.success(f"""
**Based on your profile:**
- BMR: {bmr:.0f} kcal/day (resting)
- TDEE: {tdee:.0f} kcal/day ({activity_level})
- Maintenance: {maintenance_calories:.0f} kcal/day
- Protein Target: {protein_target:.0f} g/day
- Water Target: {water_target:.1f} L/day
""")