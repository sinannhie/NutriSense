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

st.header("Personal Information")

# Age 
age = st.number_input(
    "Age",
    min_value=10,
    max_value=100,
    value=25
)

# Gender
gender = st.selectbox("Gender",["Male","Female"])
gender_encoded = 1 if gender == "Male" else 0


# Height

height = st.number_input(
    "Height (meters)",
    min_value=1.0,
    max_value=2.5,
    value=1.70,
    step=0.01
)

## Weight 
weight =st.number_input(
    "Weight (KG)",
    min_value=20.0,
    max_value=250.0,
    value=60.0,
    step=0.1
)
##Bmi
bmi = weight / (height ** 2)

st.metric(
    "BMI",
    round(bmi, 2)
)


if bmi < 18.5:
    bmi_category = "Underweight"
elif bmi < 25:
    bmi_category = "Normal Weight"
elif bmi < 30:
    bmi_category = "Overweight"
else:
    bmi_category = "Obese"

st.write(f"**BMI Category:** {bmi_category}")

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

## Eating BEtween Meels

caec = st.selectbox(
    "How Often Do You Eat Between Meals?",
    ["No", "Sometimes", "Frequently", "Always"]
)

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




if st.button("Predict Obesity Level"):

    prediction = model.predict(input_data)

    probabilities = model.predict_proba(input_data)

    predicted_class = int(prediction[0])

    result = obesity_labels[predicted_class]

    confidence = probabilities.max() * 100

    st.subheader("Prediction Results")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Predicted Category",
            result
        )

    with col2:
        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

    if result == "Insufficient Weight":
        st.warning(
            "Increase calorie intake through nutritious foods and consider strength training."
        )

    elif result == "Normal Weight":
        st.success(
            "Maintain your current lifestyle, balanced nutrition, and regular physical activity."
        )

    elif result in ["Overweight Level I", "Overweight Level II"]:
        st.warning(
            "Consider increasing physical activity and monitoring calorie intake."
        )

    else:
        st.error(
            "Consult a healthcare professional and adopt a structured nutrition and exercise plan."
       )