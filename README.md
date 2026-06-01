# NutriSense-AI

## AI-Based Obesity Risk Prediction System

NutriSense-AI is a machine learning project designed to predict obesity levels based on demographic characteristics, dietary habits, and lifestyle behaviors. The system leverages advanced machine learning algorithms to classify individuals into obesity categories and identify key health-related risk factors.

---

## Project Overview

Obesity is a growing global health concern associated with various chronic diseases. Early identification of obesity risk can help individuals make informed lifestyle and nutritional decisions.

This project analyzes health and lifestyle data to predict obesity categories using machine learning techniques and compares multiple classification algorithms to determine the most effective model.

---

## Dataset Features

The dataset includes:

* Age
* Gender
* Height
* Weight
* Family history with overweight
* Eating habits
* Physical activity level
* Water consumption
* Technology usage habits
* Transportation methods
* Other lifestyle-related factors

### Target Variable

**NObeyesdad**

Obesity Classification Categories:

* Insufficient Weight
* Normal Weight
* Overweight Level I
* Overweight Level II
* Obesity Type I
* Obesity Type II
* Obesity Type III

---

## Machine Learning Workflow

### 1. Data Preprocessing

* Data Cleaning
* Handling Categorical Variables
* Feature Encoding
* Train-Test Split
* Feature Scaling (Logistic Regression)

### 2. Exploratory Data Analysis

* Distribution Analysis
* Correlation Analysis
* Feature Relationship Exploration

### 3. Model Development

Models Evaluated:

* Logistic Regression
* Random Forest
* Tuned Random Forest
* XGBoost
* Tuned XGBoost

---

## Model Performance

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 87%      |
| Random Forest       | 96.17%   |
| Tuned Random Forest | 96.41%   |
| XGBoost             | 96.65%   |
| Tuned XGBoost       | 96.65%   |

### Best Model

**XGBoost Classifier**

Performance:

* Accuracy: 96.65%
* Macro F1 Score: 0.97
* Weighted F1 Score: 0.97

---

## Project Structure

```text
NutriSense-AI/

data/
│
└── obesity_dataset.csv

notebooks/
│
└── nutrisense_analysis_and_model_devolepment.ipynb

models/
│
└── nutrisense_xgb_model.pkl

README.md
requirements.txt
.gitignore
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* XGBoost
* Jupyter Notebook
* Joblib

---

## Future Improvements

* SHAP Explainable AI
* Streamlit Dashboard
* BMI Calculator
* BMR Calculator
* Personalized Nutrition Recommendations
* Obesity Risk Scoring System

---

## Author

Muhammed Sinan M

Data Science & Machine Learning Enthusiast

Email: [msinannhie007@gmail.com](mailto:msinannhie007@gmail.com)
