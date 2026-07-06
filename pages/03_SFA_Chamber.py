import streamlit as st

from modules.soil import SOIL_DATABASE
from modules.designer import (
    bend_thrust,
    design_chamber_support
)

st.set_page_config(
    page_title="SFA Chamber Support Designer",
    layout="wide"
)

st.title("🏗 SFA / Flow Meter Chamber Support Designer")

st.markdown("""
This tool automatically determines a suitable support block size
for a pipe bend inside an SFA or valve chamber.

### Assumed Load Path

Water Pressure

↓

Pipe Bend

↓

Concrete Support Block

↓

Base Slab

↓

Foundation Soil
""")

# Inputs

col1, col2 = st.columns(2)

with col1:

    dn = st.number_input(
        "Pipe Diameter (mm)",
        min_value=100,
        max_value=3000,
        value=600,
        step=50
    )

    pressure = st.number_input(
        "Pressure (bar)",
        min_value=1.0,
        max_value=40.0,
        value=10.0,
        step=0.5
    )

with col2:

    angle = st.selectbox(
        "Bend Angle",
        [22.5, 45, 90],
        index=2
    )

    soil = st.selectbox(
        "Soil Type",
        list(SOIL_DATABASE.keys())
    )

st.divider()

if st.button("🚀 Design Support Block", use_container_width=True):

    thrust = bend_thrust(
        diameter_mm=dn,
        pressure_bar=pressure,
        angle_deg=angle
    )

    mu = SOIL_DATABASE[soil]["mu"]

    support = design_chamber_support(
        thrust_kn=thrust,
        friction_coeff=mu
    )

    st.subheader("Results")

    left, right = st.columns(2)

    with left:

        st.metric(
            "Hydraulic Thrust (kN)",
            f"{thrust:.2f}"
        )

        st.metric(
            "Soil Friction Coefficient",
            f"{mu:.2f}"
        )

    with right:

        st.metric(
            "Risk Level",
            "LOW" if support else "HIGH"
        )

        st.metric(
            "Status",
            "SAFE ✅" if support else "NOT SAFE ❌"
        )

    st.divider()

    if support:

        st.subheader("Recommended Support Block")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Length (m)",
            support["length"]
        )

        c2.metric(
            "Width (m)",
            support["width"]
        )

        c3.metric(
            "Height (m)",
            support["height"]
        )

        st.metric(
            "Concrete Volume (m³)",
            support["volume"]
        )

        st.metric(
            "Concrete Weight (kN)",
            support["weight"]
        )

        st.metric(
            "Sliding Factor of Safety",
            support["sliding_fs"]
        )

        st.success(
            "Minimum safe support block identified."
        )

    else:

        st.error(
            "No support block found within search limits. "
            "Increase block dimensions or revise assumptions."
        )

st.divider()

st.info(
    """
    Notes:

    • Preliminary design tool only.

    • Actual chamber design should verify:
      - Sliding
      - Overturning
      - Base slab capacity
      - Passive soil resistance
      - Reinforcement

    • Final design should be reviewed by Mechanical,
      Civil and Geotechnical Engineers.
    """
)
