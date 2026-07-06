import streamlit as st
import matplotlib.pyplot as plt

from modules.thrust import bend_thrust
from modules.chamber_support import design_support_block

st.set_page_config(
    page_title="SFA Chamber Thrust block Designer",
    page_icon="👷🏼",
    layout="wide"
)

# =====================================================
# HEADER
# =====================================================

col1, col2 = st.columns([6, 1])

with col1:
    st.title("🏗 SFA Chamber Concrete Support Designer")

with col2:
    st.image(
        "assets/logo.png",
        width=120
    )

st.caption(
    "Preliminary Design Tool for Flow Meter and Valve Chamber concrete Support Blocks"
)

st.caption(
    "SFA Chamber often refers to a chamber required under Sewers for Adoption (SfA) standards (UK wastewater infrastructure). "
)

# =====================================================
# CONCRETE DATABASE
# =====================================================

CONCRETE_DATA = {
    "C25/30": {
        "fck": 25,
        "bearing": 500,
        "description": "General purpose concrete."
    },
    "C30/37": {
        "fck": 30,
        "bearing": 600,
        "description": "Recommended for most flow meter and valve chambers."
    },
    "C40/50": {
        "fck": 40,
        "bearing": 800,
        "description": "Heavy-duty concrete."
    }
}

# =====================================================
# INPUTS
# =====================================================

st.header("Design Inputs")

c1, c2 = st.columns(2)

with c1:

    diameter = st.number_input(
        "Pipe Diameter (mm)",
        min_value=100,
        max_value=3000,
        value=800
    )

    pressure = st.number_input(
        "Pressure (bar)",
        min_value=1.0,
        max_value=40.0,
        value=16.0
    )

    angle = st.selectbox(
        "Bend Angle",
        [11.25, 22.5, 45, 90]
    )

with c2:

    concrete_grade = st.selectbox(
        "Concrete Grade",
        [
            "C25/30",
            "C30/37",
            "C40/50"
        ],
        index=1
    )

    design_class = st.selectbox(
        "Design Classification",
        [
            "Standard",
            "Critical",
            "Emergency Service"
        ]
    )

# =====================================================
# WATER HAMMER
# =====================================================

water_hammer = st.checkbox(
    "Include Water Hammer / Surge Pressure"
)

# =====================================================
# CHAMBER DIMENSIONS
# =====================================================

st.header("Chamber Dimensions")

cc1, cc2, cc3 = st.columns(3)

with cc1:
    chamber_length = st.number_input(
        "Length (m)",
        value=3.0
    )

with cc2:
    chamber_width = st.number_input(
        "Width (m)",
        value=2.5
    )

with cc3:
    chamber_depth = st.number_input(
        "Depth (m)",
        value=2.0
    )

# =====================================================
# REINFORCEMENT OPTION
# =====================================================

steel_type = st.selectbox(
    "Reinforcement Density",
    [
        "Light RCC (0-100 kg/m³)",
        "Standard RCC (100-180 kg/m³)",
        "Heavy RCC (180-250 kg/m³)"
    ]
)


# Representative reinforcement densities for estimation

STEEL_DENSITY = {
    "Light RCC (0-100 kg/m³)": 100,
    "Standard RCC (100-180 kg/m³)": 180,
    "Heavy RCC (180-250 kg/m³)": 250
}

steel_density = STEEL_DENSITY[steel_type]

st.write(f"Selected Reinforcement Density: {steel_density} kg/m³")

# =====================================================
# CONCRETE GRADE HELP
# =====================================================

with st.expander("📘 Concrete Grade Guide"):

    st.markdown("""
### C25/30

- General civil works
- Pipe supports
- Small chambers

---

### C30/37 (Recommended)

- Flow meter chambers
- Valve chambers
- Water infrastructure

---

### C40/50

- Pump stations
- High-load structures
- Critical infrastructure

✅ Recommended for most SFA chambers: C30/37
""")

# =====================================================
# DESIGN BUTTON
# =====================================================

if st.button(
    "🚀 Design Support Block",
    use_container_width=True
):

    thrust = bend_thrust(
        diameter,
        pressure,
        angle
    )

    safety_factor_table = {
        "Standard": 1.5,
        "Critical": 2.0,
        "Emergency Service": 2.5
    }

    sf = safety_factor_table[
        design_class
    ]

    hammer_factor = 1.3 if water_hammer else 1.0

    design_thrust = (
        thrust
        * sf
        * hammer_factor
    )

    result = design_support_block(
        design_thrust,
        concrete_grade
    )

    concrete_volume = result["volume"]

    steel_weight = (
        concrete_volume
        * STEEL_DENSITY[steel_type]
    )

    # =================================================
    # DESIGN SUMMARY DASHBOARD
    # =================================================

    st.header("Design Summary")

    d1, d2, d3 = st.columns(3)

    d1.metric(
        "Hydraulic Thrust",
        f"{thrust:.1f} kN"
    )

    d2.metric(
        "Design Thrust",
        f"{design_thrust:.1f} kN"
    )

    d3.metric(
        "Safety Factor",
        f"{sf:.2f}"
    )

    d4, d5, d6 = st.columns(3)

    d4.metric(
        "Required Area",
        f"{result['required_area']:.2f} m²"
    )

    d5.metric(
        "Concrete Volume",
        f"{concrete_volume:.2f} m³"
    )

    d6.metric(
        "Estimated Steel",
        f"{steel_weight:.0f} kg"
    )

    # =================================================
    # BLOCK SIZE
    # =================================================

    st.header("Recommended Support Block")

    b1, b2, b3 = st.columns(3)

    b1.metric(
        "Length",
        f"{result['length']} m"
    )

    b2.metric(
        "Width",
        f"{result['width']} m"
    )

    b3.metric(
        "Height",
        f"{result['height']} m"
    )

    # =================================================
    # RCC ESTIMATE
    # =================================================

    st.header("Quantity Estimate")

    st.write(
        f"Concrete Quantity : {concrete_volume:.2f} m³"
    )

    st.write(
        f"Estimated Reinforcement : {steel_weight:.0f} kg"
    )

    # =================================================
    # DOWNLOAD REPORT
    # =================================================

    report = f"""
PIPELINE THRUST BLOCK DESIGN REPORT

Pipe Diameter : {diameter} mm

Pressure : {pressure} bar

Bend Angle : {angle}°

Concrete Grade : {concrete_grade}

Design Classification : {design_class}

Water Hammer Included : {water_hammer}

Hydraulic Thrust : {thrust:.2f} kN

Design Thrust : {design_thrust:.2f} kN

Recommended Support Block

Length : {result['length']} m

Width : {result['width']} m

Height : {result['height']} m

Required Area : {result['required_area']} m²

Concrete Volume : {concrete_volume:.2f} m³

Estimated Reinforcement : {steel_weight:.0f} kg
"""

    st.download_button(
        "📄 Download Report",
        report,
        file_name="SFA_Support_Report.txt",
        mime="text/plain"
    )

# 24. Disclaimer

This tool is intended for: Preliminary design only. Results should be verified against project specifications, geotechnical data, and applicable standards before construction.

✅ Preliminary Design

✅ Concept Design

✅ Budget Estimating

✅ Design Review

✅ Engineering Verification

Final designs must always be reviewed by qualified Mechanical, Civil and Geotechnical Engineers and verified against project specifications and local standards.
""")
