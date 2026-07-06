import streamlit as st

st.set_page_config(
    page_title="Risk Assessment",
    page_icon="⚠️",
    layout="wide"
)

# =====================================================
# HEADER
# =====================================================

col1, col2 = st.columns([6, 1])

with col1:
    st.title("⚠️ Risk Assessment")

with col2:
    try:
        st.image(
            "assets/logo.png",
            width=120
        )
    except:
        pass

st.caption(
    "Engineering risk assessment for pipeline thrust block design"
)

# =====================================================
# INPUTS
# =====================================================

st.header("Assessment Inputs")

c1, c2 = st.columns(2)

with c1:

    pressure = st.number_input(
        "Operating Pressure (bar)",
        min_value=1.0,
        max_value=50.0,
        value=10.0
    )

    soil = st.selectbox(
        "Soil Type",
        [
            "Soft Clay",
            "Medium Clay",
            "Stiff Clay",
            "Dense Sand",
            "Gravel",
            "Rock"
        ]
    )

with c2:

    water_hammer = st.selectbox(
        "Water Hammer Condition",
        [
            "None",
            "Mild Surge (+10%)",
            "Moderate Surge (+20%)",
            "Severe Surge (+30%)"
        ]
    )

    safety_factor = st.selectbox(
        "Safety Factor",
        [1.5, 2.0, 2.5],
        index=1
    )

required_area = st.number_input(
    "Required Thrust Block Area (m²)",
    min_value=0.1,
    value=3.0
)

# =====================================================
# CALCULATE
# =====================================================

if st.button(
    "🚀 Run Risk Assessment",
    use_container_width=True
):

    # -----------------------------------------
    # Pressure Risk
    # -----------------------------------------

    if pressure < 10:
        pressure_risk = "LOW"
        pressure_score = 1

    elif pressure <= 16:
        pressure_risk = "MEDIUM"
        pressure_score = 2

    elif pressure <= 25:
        pressure_risk = "HIGH"
        pressure_score = 3

    else:
        pressure_risk = "CRITICAL"
        pressure_score = 4

    # -----------------------------------------
    # Soil Risk
    # -----------------------------------------

    soil_scores = {
        "Rock": ("LOW", 1),
        "Gravel": ("LOW", 1),
        "Dense Sand": ("MEDIUM", 2),
        "Stiff Clay": ("MEDIUM", 2),
        "Medium Clay": ("HIGH", 3),
        "Soft Clay": ("CRITICAL", 4)
    }

    soil_risk, soil_score = soil_scores[soil]

    # -----------------------------------------
    # Water Hammer Risk
    # -----------------------------------------

    hammer_scores = {
        "None": ("LOW", 1),
        "Mild Surge (+10%)": ("MEDIUM", 2),
        "Moderate Surge (+20%)": ("HIGH", 3),
        "Severe Surge (+30%)": ("CRITICAL", 4)
    }

    hammer_risk, hammer_score = hammer_scores[water_hammer]

    # -----------------------------------------
    # Area Risk
    # -----------------------------------------

    if required_area < 2:
        area_risk = "LOW"
        area_score = 1

    elif required_area < 5:
        area_risk = "MEDIUM"
        area_score = 2

    elif required_area < 10:
        area_risk = "HIGH"
        area_score = 3

    else:
        area_risk = "CRITICAL"
        area_score = 4

    # -----------------------------------------
    # Safety Factor Risk
    # -----------------------------------------

    if safety_factor >= 2.5:
        sf_risk = "LOW"
        sf_score = 1

    elif safety_factor >= 2.0:
        sf_risk = "MEDIUM"
        sf_score = 2

    else:
        sf_risk = "HIGH"
        sf_score = 3

    # -----------------------------------------
    # Overall Risk
    # -----------------------------------------

    total_score = (
        pressure_score
        + soil_score
        + hammer_score
        + area_score
        + sf_score
    )

    if total_score <= 8:
        overall_risk = "LOW"

    elif total_score <= 12:
        overall_risk = "MEDIUM"

    elif total_score <= 16:
        overall_risk = "HIGH"

    else:
        overall_risk = "CRITICAL"

    # =================================================
    # DASHBOARD
    # =================================================

    st.header("Risk Dashboard")

    r1, r2, r3 = st.columns(3)

    r1.metric(
        "Pressure Risk",
        pressure_risk
    )

    r2.metric(
        "Soil Risk",
        soil_risk
    )

    r3.metric(
        "Water Hammer Risk",
        hammer_risk
    )

    r4, r5, r6 = st.columns(3)

    r4.metric(
        "Block Size Risk",
        area_risk
    )

    r5.metric(
        "Safety Factor Risk",
        sf_risk
    )

    r6.metric(
        "Overall Risk",
        overall_risk
    )

    # =================================================
    # RESULT
    # =================================================

    st.header("Overall Assessment")

    if overall_risk == "LOW":
        st.success(
            "✅ LOW RISK - Design appears robust for preliminary sizing."
        )

    elif overall_risk == "MEDIUM":
        st.info(
            "🟡 MEDIUM RISK - Engineering review recommended."
        )

    elif overall_risk == "HIGH":
        st.warning(
            "🟠 HIGH RISK - Additional verification is recommended."
        )

    else:
        st.error(
            "🔴 CRITICAL RISK - Detailed review and redesign recommended."
        )

    # =================================================
    # RECOMMENDATIONS
    # =================================================

    st.header("Engineering Recommendations")

    recommendations = []

    if soil == "Soft Clay":
        recommendations.append(
            "Obtain a geotechnical investigation report."
        )

    if pressure > 16:
        recommendations.append(
            "Verify surge and thrust loading assumptions."
        )

    if water_hammer == "Severe Surge (+30%)":
        recommendations.append(
            "Perform detailed transient surge analysis."
        )

    if required_area > 8:
        recommendations.append(
            "Consider restrained joints to reduce thrust block size."
        )

    if safety_factor < 2.0:
        recommendations.append(
            "Consider increasing the safety factor."
        )

    if not recommendations:
        recommendations.append(
            "No major design concerns identified."
        )

    for item in recommendations:
        st.warning(item)

    # =================================================
    # REPORT DOWNLOAD
    # =================================================

    report = f"""
PIPELINE THRUST BLOCK RISK ASSESSMENT

Pressure Risk: {pressure_risk}

Soil Risk: {soil_risk}

Water Hammer Risk: {hammer_risk}

Block Size Risk: {area_risk}

Safety Factor Risk: {sf_risk}

Overall Risk: {overall_risk}

Total Risk Score: {total_score}
"""

    st.download_button(
        "📄 Download Risk Report",
        report,
        file_name="Risk_Assessment_Report.txt",
        mime="text/plain"
    )

# =====================================================
# DISCLAIMER
# =====================================================

# 24. Disclaimer

This tool is intended for: Preliminary design only. Results should be verified against project specifications, geotechnical data, and applicable standards before construction.

✅ Preliminary Design

✅ Concept Design

✅ Budget Estimating

✅ Design Review

✅ Engineering Verification

Final designs must always be reviewed by qualified Mechanical, Civil and Geotechnical Engineers and verified against project specifications and local standards.
""")
