import streamlit as st
import joblib

model = joblib.load("models/nutrisense_xgb_model.pkl")
obesity_labels = {
    0: "Insufficient Weight",
    1: "Normal Weight",
    2: "Overweight Level I",
    3: "Overweight Level II",
    4: "Obesity Type I",
    5: "Obesity Type II",
    6: "Obesity Type III"
}


st.set_page_config(
    page_title="NutriSense",
    page_icon="🥗",
    layout="centered"
)

st.title("🥗 NutriSense")
st.subheader("Machine Learning-Based Obesity Risk Prediction System")

st.markdown("---")

st.write(
    "Predict obesity levels using demographic, dietary, and lifestyle information."
)

st.header("👤 Personal Information")

# Age & Gender 
col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age",
        min_value=10,
        max_value=100,
        value=25
    )

with col2:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

gender_encoded = 1 if gender == "Male" else 0


# Height & weight 
col1, col2 =st.columns(2)

with col1:
    height = st.number_input(
    "Height (meters)",
    min_value=1.0,
    max_value=2.5,
    value=1.70,
    step=0.01
)

with col2: 
    weight =st.number_input(
    "Weight (KG)",
    min_value=20.0,
    max_value=250.0,
    value=60.0,
    step=0.1
)
##Bmi

st.header("📈 Health Metrics")

bmi = weight / (height ** 2)


col1,col2 =st.columns(2)
with col1:
         st.metric(
        "BMI",
        f"{bmi:.2f}"
    )


if bmi < 18.5:
    bmi_category = "Underweight"
elif bmi < 25:
    bmi_category = "Normal Weight"
elif bmi < 30:
    bmi_category = "Overweight"
else:
    bmi_category = "Obese"

with col2:
        st.metric(
        "BMI Category",
        bmi_category
    )

st.markdown("---")

st.header("🍽️ Eating Habits")

## Family History



family_history = st.selectbox(
    "Family History of Overweight",
    ["Yes", "No"]
)

family_history_encoded = 1 if family_history == "Yes" else 0


## CAlorie Consumption
favc = st.selectbox(
    "Do you frequently consume high-calorie foods?",
    ["Yes", "No"]
)

favc_encoded = 1 if favc == "Yes" else 0


## Frequency of Vegetable Consumption

fcvc = st.slider(
    "How often do you consume vegetables?",
    min_value=1.0,
    max_value=3.0,
    value=2.0,
    step=0.1
)

## Number of Main Meals Per Day

ncp = st.slider(
    "Number of Main Meals Per Day",
    min_value=1.0,
    max_value=4.0,
    value=3.0,
    step=0.1
)

## Eating BEtween Meels

caec = st.selectbox(
    "How Often Do You Eat Between Meals?",
    ["No", "Sometimes", "Frequently", "Always"]
)

st.header("🏃 Lifestyle Information")

## Daily Water Consumption

ch2o = st.slider(
    "Daily Water Consumption (Litres)",
    min_value=1.0,
    max_value=3.0,
    value=2.0,
    step=0.1
)

## Physical Activity Frequency

faf = st.slider(
    "Physical Activity Frequency",
    min_value=0.0,
    max_value=3.0,
    value=1.0,
    step=0.1
)



## Time Using Technology Devices

tue = st.slider(
    "Daily Technology Usage",
    min_value=0.0,
    max_value=2.0,
    value=1.0,
    step=0.1
)

## Smoke

smoke = st.selectbox(
    "Do You Smoke?",
    ["No", "Yes"]
)

smoke_encoded = 1 if smoke == "Yes" else 0


## Calorie Monitoring

scc = st.selectbox(
    "Do You Monitor Your Calorie Consumption?",
    ["No", "Yes"]
)

scc_encoded = 1 if scc == "Yes" else 0



caec_encoded = {
    "No": 0,
    "Sometimes": 1,
    "Frequently": 2,
    "Always": 3
}[caec]

## Transportation 

mtrans = st.selectbox(
    "Primary Mode of Transportation",
    [
        "Walking",
        "Bike",
        "Motorbike",
        "Public Transportation",
        "Automobile"
    ]
)

mtrans_encoded = {
    "Walking": 0,
    "Bike": 1,
    "Motorbike": 2,
    "Public Transportation": 3,
    "Automobile": 4
}[mtrans]

## Alcohol Consumption

calc = st.selectbox(
    "Alcohol Consumption",
    ["No", "Sometimes", "Frequently", "Always"]
)

calc_encoded = {
    "No": 0,
    "Sometimes": 1,
    "Frequently": 2,
    "Always": 3
}[calc]



## Input Data order 

import pandas as pd

input_data = pd.DataFrame([{
    "Age": age,
    "Gender": gender_encoded,
    "Height": height,
    "Weight": weight,
    "CALC": calc_encoded,
    "FAVC": favc_encoded,
    "FCVC": fcvc,
    "NCP": ncp,
    "SCC": scc_encoded,
    "SMOKE": smoke_encoded,
    "CH2O": ch2o,
    "family_history_with_overweight": family_history_encoded,
    "FAF": faf,
    "TUE": tue,
    "CAEC": caec_encoded,
    "MTRANS": mtrans_encoded
}])



predict = st.button(
    "🔍 Predict Obesity Level",
    use_container_width=True
)

if predict:

    prediction = model.predict(input_data)
    probabilities = model.predict_proba(input_data)

    predicted_class = int(prediction[0])

    result = obesity_labels[predicted_class]
    confidence = probabilities.max() * 100

    st.header("📊 Prediction Results")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Predicted Category",
            value=result
        )

    with col2:
        st.metric(
            label="Confidence",
            value=f"{confidence:.2f}%"
        )

    st.header("📊 Health Assessment")

    if result == "Insufficient Weight":

        st.warning(
            "⚠️ Increase calorie intake through nutritious foods and consider strength training."
        )

    elif result == "Normal Weight":

        st.success(
            "✅ Maintain your current lifestyle, balanced nutrition, and regular physical activity."
        )

    elif result in ["Overweight Level I", "Overweight Level II"]:

        st.warning(
            "⚠️ Consider increasing physical activity and monitoring calorie intake."
        )

    else:

        st.error(
            "🚨 Consult a healthcare professional and adopt a structured nutrition and exercise plan."
        )

    st.markdown("---")

    st.header("🧠 AI Health Insights")

    recommendations = []

    # BMI Recommendations

    if bmi < 18.5:
        recommendations.append(
            "Increase calorie intake through nutrient-dense foods."
        )

    elif bmi < 25:
        recommendations.append(
            "Maintain your current body weight through balanced nutrition."
        )

    elif bmi < 30:
        recommendations.append(
            "Consider a moderate calorie deficit to support healthy weight loss."
        )

    else:
        recommendations.append(
            "Focus on structured weight management through nutrition and exercise."
        )

    # Physical Activity Recommendations

    if faf < 1:
        recommendations.append(
            "Increase physical activity levels to improve overall health and weight management."
        )

    elif faf < 2:
        recommendations.append(
            "Aim for at least 30 minutes of moderate exercise most days of the week."
        )

    else:
        recommendations.append(
            "Maintain your current physical activity routine."
        )

    # Water Intake Recommendations

    if ch2o < 1.5:
        recommendations.append(
            "Increase daily water intake to at least 2 liters per day."
        )

    elif ch2o < 2.5:
        recommendations.append(
            "Your hydration level is adequate. Continue maintaining good water intake."
        )

    else:
        recommendations.append(
            "Excellent hydration habits. Continue drinking sufficient water daily."
        )

    # Prediction-Based Recommendations

    if result == "Insufficient Weight":

        recommendations.append(
            "Focus on increasing calorie and protein intake through healthy foods."
        )

    elif result == "Normal Weight":

        recommendations.append(
            "Continue your current lifestyle to maintain a healthy weight."
        )

    elif result == "Overweight Level I":

        recommendations.append(
            "A moderate calorie deficit and increased activity can help prevent further weight gain."
        )

    elif result == "Overweight Level II":

        recommendations.append(
            "Consider a structured weight-loss plan combining nutrition and exercise."
        )

    elif result == "Obesity Type I":

        recommendations.append(
            "Focus on gradual and sustainable weight reduction with professional guidance if needed."
        )

    elif result == "Obesity Type II":

        recommendations.append(
            "Consult a healthcare professional for a comprehensive weight management strategy."
        )

    elif result == "Obesity Type III":

        recommendations.append(
            "Medical supervision is strongly recommended alongside nutrition and lifestyle interventions."
        )

    

    for rec in recommendations:
        st.info(f"- {rec}")