
import streamlit as st
import plotly.graph_objects as go

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    HRFlowable
)

from reportlab.lib.styles import getSampleStyleSheet

import io

from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)

st.set_page_config(
    page_title="NutriSense",
    page_icon="🥗",
    layout="wide"
)


st.title("🔥 Nutrition Analytics")

## Stylee
st.markdown("""
<style>

.kpi-card{
    background: linear-gradient(135deg,#0f172a,#1e293b);
    padding:20px;
    border-radius:18px;
    text-align:center;
    border:1px solid #334155;
    box-shadow:0 4px 12px rgba(0,0,0,0.15);
}

.kpi-title{
    font-size:16px;
    color:#94a3b8;
    margin-bottom:10px;
}

.kpi-value{
    font-size:32px;
    font-weight:700;
    color:white;
}

.kpi-unit{
    font-size:14px;
    color:#cbd5e1;
}

</style>
""", unsafe_allow_html=True)
## Style kpi calorie bar

st.markdown("""
<style>

.kpi-up{
    color:#22c55e;
    font-weight:700;
}

.kpi-down{
    color:#ef4444;
    font-weight:700;
}

.kpi-neutral{
    color:#94a3b8;
    font-weight:700;
}

</style>
""", unsafe_allow_html=True)

### Banner csss
st.markdown("""
<style>

.summary-card{
    background: linear-gradient(135deg,#0f172a,#1e293b);
    border-radius:20px;
    padding:25px;
    margin-bottom:20px;
    border:1px solid #334155;
}

.summary-title{
    font-size:28px;
    font-weight:700;
    color:white;
}

.summary-subtitle{
    font-size:16px;
    color:#cbd5e1;
}

.summary-highlight{
    color:#4ade80;
    font-weight:700;
}

</style>
""", unsafe_allow_html=True)

## Halth card css

st.markdown("""
<style>

.health-card{
    background: linear-gradient(135deg,#0f172a,#1e293b);
    border-radius:20px;
    padding:30px;
    text-align:center;
    margin-bottom:20px;
    border:1px solid #334155;
}

.health-score{
    font-size:64px;
    font-weight:800;
}

.health-status{
    font-size:20px;
    font-weight:600;
    margin-top:10px;
}

</style>
""", unsafe_allow_html=True)


### ---------------------------------------------------------------------


faf = st.session_state.get("faf")
ch2o = st.session_state.get("ch2o")
confidence = st.session_state.get("confidence")
report = st.session_state.get("report_data", {})



## Round


bmi = round(st.session_state.get("bmi", 0), 2)
bmr = round(st.session_state.get("bmr", 0))
weight = round(st.session_state.get("weight", 0), 1)




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



health_score = 100

# BMI
if bmi < 18.5:
    health_score -= 15
elif bmi > 25:
    health_score -= 15

# Water
if water_target < 2:
    health_score -= 10

# Activity
if faf < 1:
    health_score -= 15

health_score = max(0, min(100, health_score))

## round calc


tdee = round(tdee)

protein_target = round(protein_target)

water_target = round(water_target, 1)


## health status conditio

if health_score >= 90:
    health_status = "Excellent"
    score_color = "#22c55e"

elif health_score >= 75:
    health_status = "Good"
    score_color = "#3b82f6"

elif health_score >= 60:
    health_status = "Fair"
    score_color = "#f59e0b"

else:
    health_status = "Needs Improvement"
    score_color = "#ef4444"

    
### Banner 

col1, col2 = st.columns([3,1])

with col1:
    st.markdown(f"""
    <div class="summary-card">

    <div class="summary-title">
    👤 {report.get('client_name', 'User')}
    </div>

    <div class="summary-subtitle">
    🎯 <span class="summary-highlight">
    {report.get('prediction', 'N/A')}
    </span>
    </div>

    <br>

    <div class="summary-subtitle">
    📊 Confidence: <span class="summary-highlight">
    {report.get('confidence', 'N/A')}%
    </span>
    </div>

    <div class="summary-subtitle">
    🏃 Activity Level:
    <span class="summary-highlight">
    {activity_level}
    </span>
    </div>

    <div class="summary-subtitle">
    📅 Report ID:
    <span class="summary-highlight">
    {report.get('report_id', 'Generating...')}
    </span>
    </div>

    </div>
    """, unsafe_allow_html=True)
    
    

with col2:
    # health score card

    st.markdown(f"""
    <div class="health-card">

    <div style="color:white;font-size:20px;">
    🏆 Health Score
    </div>

    <div class="health-score"
     style="color:{score_color};">
     {health_score}
    </div>

    <div class="health-status"
         style="color:{score_color};">
         {health_status}
    </div>

    </div>
    """, unsafe_allow_html=True)


# --- Section 1: Base Metrics ---
st.subheader("📊 Health Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">⚖️ BMI</div>
        <div class="kpi-value">{bmi}</div>
        <div class="kpi-unit">Body Mass Index</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">🔥 BMR</div>
        <div class="kpi-value">{bmr}</div>
        <div class="kpi-unit">kcal/day</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">⚡ TDEE</div>
        <div class="kpi-value">{tdee}</div>
        <div class="kpi-unit">kcal/day</div>
    </div>
    """, unsafe_allow_html=True)

## Health profioe charttt
import plotly.express as px
import pandas as pd

st.markdown("---")

st.subheader("🩺 Health Profile Overview")

# Scores

bmi_score = 100 if 18.5 <= bmi <= 24.9 else 60

activity_score = {
    "Sedentary": 50,
    "Lightly Active": 75,
    "Moderately Active": 90,
    "Very Active": 100
}.get(activity_level, 50)

hydration_score = min(
    int((water_target / 3) * 100),
    100
)

nutrition_score = min(
    int((protein_target / 120) * 100),
    100
)

health_df = pd.DataFrame({
    "Metric": [
        "BMI Health",
        "Activity",
        "Hydration",
        "Nutrition"
    ],
    "Score": [
        bmi_score,
        activity_score,
        hydration_score,
        nutrition_score
    ]
})

fig = px.bar(
    health_df,
    x="Metric",
    y="Score",
    text="Score",
    color="Score",
    color_continuous_scale="Viridis"
)

fig.update_layout(
    height=350,
    showlegend=False,
    coloraxis_showscale=False,
    margin=dict(l=20,r=20,t=20,b=20)
)

fig.update_traces(
    textposition="outside"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
# --- Section 2: Calorie Goals ---

st.subheader("🎯 Calorie Goals")


col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">⚖️ Maintenance</div>
        <div class="kpi-value">{maintenance_calories:.0f}</div>        
        <div class="kpi-unit kpi-neutral">
            ➖ Maintenance Level </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">📉 Fat Loss</div>
        <div class="kpi-value">{fat_loss_calories:.0f}</div>
        <div class="kpi-unit kpi-down">
        ▼ -500 kcal Deficit
        </div>

    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">💪 Muscle Gain</div>
        <div class="kpi-value">{muscle_gain_calories:.0f}</div>
        <div class="kpi-unit kpi-up">
          ▲ +300 kcal Surplus
        </div>
    </div>
    """, unsafe_allow_html=True)


st.markdown("---")

st.subheader("📊 Calorie Goal Comparison")

calorie_df = pd.DataFrame({
    "Goal": [
        "Fat Loss",
        "Maintenance",
        "Muscle Gain"
    ],
    "Calories": [
        fat_loss_calories,
        maintenance_calories,
        muscle_gain_calories
    ]
})

fig = px.bar(
    calorie_df,
    y="Goal",
    x="Calories",
    orientation="h",
    text="Calories",
    color="Goal"
)

fig.update_layout(
    height=350,
    showlegend=False,
    margin=dict(l=20,r=20,t=20,b=20)
)

fig.update_traces(
    textposition="outside"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# --- Section 3: Nutrition Targets ---
st.subheader("🥗 Daily Nutrition Targets")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">🍗 Protein Target</div>
        <div class="kpi-value">{protein_target}</div>
        <div class="kpi-unit" style="color:#22c55e;">
            ▲ Muscle Recovery & Growth
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">💧 Water Target</div>
        <div class="kpi-value">{water_target}</div>
        <div class="kpi-unit" style="color:#3b82f6;">
            ▲ Daily Hydration Goal
        </div>
    </div>
    """, unsafe_allow_html=True)

## visualo

# REPORT PREVIEW + PDF GENERATION


from datetime import datetime

# Update report data

report_id = datetime.now().strftime(
    "NS-%Y%m%d-%H%M"
)

if "report_data" in st.session_state:

    st.session_state["report_data"].update({

        "tdee": round(tdee),

        "protein_target": round(protein_target),

        "water_target": round(water_target, 1),

        "report_id": report_id

    })





# ==========================
# PDF GENERATION
# ==========================
def create_pdf(report):

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    content = []

    # ==========================
    # CLEAN VALUES
    # ==========================

    bmi = round(float(report.get("bmi", 0)), 2)

    confidence = round(
        float(report.get("confidence", 0)), 2
    )

    bmr = round(
        float(report.get("bmr", 0))
    )

    tdee = round(
        float(report.get("tdee", 0))
    )

    protein = round(
        float(report.get("protein_target", 0))
    )

    water = round(
        float(report.get("water_target", 0)), 1
    )
    height_cm = float(report.get("height",0))*100

    # ==========================
    # TITLE
    # ==========================

    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        fontSize=24,
        alignment=1,
        textColor=colors.HexColor("#0F172A")
    )

    subtitle_style = ParagraphStyle(
        "Subtitle",
        parent=styles["Normal"],
        alignment=1,
        textColor=colors.grey
    )

    content.append(
        Paragraph(
            "🥗 NutriSense AI Health Report",
            title_style
        )
    )
    content.append(
        Paragraph(
            "Personal Health Assessment Report",
            subtitle_style
        )
    )
    content.append(
        Paragraph(
            "AI-Powered Obesity Risk Assessment & Nutrition Analytics",
            subtitle_style
        )
    )

    content.append(Spacer(1, 20))

    # ==========================
    # REPORT INFO
    # ==========================

    content.append(
        Paragraph(
            f"<b>Report ID:</b> {report.get('report_id','N/A')}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Generated On:</b> {datetime.now().strftime('%d %B %Y')}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 15))

    # ==========================
    # CLIENT TABLE
    # ==========================

    content.append(
        Paragraph(
            "Client Information",
            styles["Heading2"]
        )
    )

    client_data = [

        ["Field", "Value"],

        ["Client Name",
         report.get("client_name", "N/A")],

        ["Age",
         report.get("age", "N/A")],

        ["Gender",
         report.get("gender", "N/A")],

        ["Weight",
         f"{report.get('weight','N/A')} kg"],

        ["Height",
         f"{float(report.get('height', 0)) * 100:.0f} cm"]
        

    ]

    client_table = Table(
        client_data,
        colWidths=[180, 220]
    )

    client_table.setStyle(
        TableStyle([
            ("ROWBACKGROUNDS",(0,1),(-1,-1),
            [colors.whitesmoke, colors.lightgrey]),

            ("BACKGROUND",(0,0),(-1,0),
             colors.HexColor("#2563EB")),

            ("TEXTCOLOR",(0,0),(-1,0),
             colors.white),

            ("GRID",(0,0),(-1,-1),
             1,colors.black),

            ("FONTNAME",(0,0),(-1,0),
             "Helvetica-Bold"),
            ("FONTSIZE",(0,0),(-1,0),12),
            ("BOTTOMPADDING",(0,0),(-1,0),12),
            ("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke)

        ])
    )

    content.append(client_table)

    content.append(Spacer(1, 20))

    # ==========================
    # PREDICTION
    # ==========================

    prediction_style = ParagraphStyle(
        "PredictionStyle",
        parent=styles["Heading2"],
        alignment=1,
        textColor=colors.green
    )

    content.append(
        Paragraph(
            "Obesity Assessment",
            styles["Heading2"]
        )
    )

    prediction_data = [

        ["Prediction",
         report.get("prediction", "N/A")],

        ["Confidence",
         f"{confidence}%"]

    ]

    prediction_table = Table(
        prediction_data,
        colWidths=[180,220]
    )

    prediction_table.setStyle(
        TableStyle([

            

            ("BACKGROUND",(0,0),(-1,-1),
             colors.HexColor("#E8F5E9")),

            ("GRID",(0,0),(-1,-1),
             1,colors.black),

            ("FONTNAME",(0,0),(-1,-1),
             "Helvetica-Bold"),
            
            ("FONTSIZE",(0,0),(-1,0),12),
            ("BOTTOMPADDING",(0,0),(-1,0),12),
            ("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke)

        ])
    )

    content.append(prediction_table)

    content.append(Spacer(1, 20))

    # ==========================
    # HEALTH METRICS
    # ==========================

    content.append(
        Paragraph(
            "Health Metrics",
            styles["Heading2"]
        )
    )

    metrics_data = [

        ["Metric", "Value"],
        ["Health Score", "100 / 100"],

        ["BMI", bmi],

        ["BMR",
         f"{bmr} kcal/day"],

        ["TDEE",
         f"{tdee} kcal/day"],

        ["Protein Target",
         f"{protein} g/day"],

        ["Water Target",
         f"{water} L/day"]

    ]

    metrics_table = Table(
        metrics_data,
        colWidths=[180,220]
    )

    metrics_table.setStyle(
        TableStyle([

            ("BACKGROUND",(0,0),(-1,0),
             colors.HexColor("#0EA5E9")),

            ("TEXTCOLOR",(0,0),(-1,0),
             colors.white),

            ("GRID",(0,0),(-1,-1),
             1,colors.black),

            ("FONTNAME",(0,0),(-1,0),
             "Helvetica-Bold")

        ])
    )

    content.append(metrics_table)

    content.append(Spacer(1, 20))

    # ==========================
    # HEALTH SUMMARY
    # ==========================

    content.append(
        Paragraph(
            "Health Summary",
            styles["Heading2"]
        )
    )

    summary = f"""
    <b>Prediction:</b> {report.get('prediction','N/A')}<br/><br/>

    Your BMI is <b>{bmi}</b>, indicating your current
    health classification based on body composition.

    <br/><br/>

    Estimated daily energy expenditure is
    <b>{tdee} kcal/day</b>.

    <br/><br/>

    Recommended daily protein intake:
    <b>{protein} g/day</b>.

    <br/><br/>

    Recommended water intake:
    <b>{water} L/day</b>.

    <br/><br/>

    Model confidence:
    <b>{confidence}%</b>.
    """

    content.append(
        Paragraph(
            summary,
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 30))

    # ==========================
    # FOOTER
    # ==========================

    footer_style = ParagraphStyle(
        "Footer",
        parent=styles["Italic"],
        alignment=1,
        textColor=colors.grey
    )
    content.append(
        Spacer(1,20)
    )

    content.append(
        HRFlowable(
            width="100%",
            thickness=1,
            color=colors.grey
        )
    )
    content.append(
        Paragraph(
            "This report is intended for educational purposes and should not replace professional medical advice",
            footer_style
        )
    )

    content.append(
        Paragraph(
            "Generated by NutriSense AI",
            footer_style
        )
    )

    content.append(
        Paragraph(
            "Machine Learning Powered Health Analytics Platform",
            footer_style
        )
    )

    doc.build(content)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf

# ==========================
# DOWNLOAD
# ==========================
st.markdown("---")

st.subheader("📥 Download Health Report")

report = st.session_state.get(
    "report_data",
    {}
)

pdf = create_pdf(report)

pdf_filename = (
    f"NutriSense_"
    f"{report.get('client_name','User')}_"
    f"{report.get('report_id','Report')}.pdf"
)

st.download_button(
    label="📄 Download PDF Report",
    data=pdf,
    file_name=pdf_filename,
    mime="application/pdf",
    use_container_width=True
)