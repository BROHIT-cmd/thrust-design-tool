import streamlit as st

from modules.designer import bend_thrust
from modules.chamber_support import support_block_design

st.set_page_config(
    page_title="SFA Chamber Support Designer",
    layout="wide"
)

st.title("🏗 SFA Chamber Support Designer")

st.markdown("""
This tool sizes a concrete support block that transfers
hydraulic thrust from a pipe bend into the chamber slab.

Load Path:

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

col1, col2 = st.columns(2)

with col1:

    diameter = st.number_input(
        "Pipe Diameter (mm)",
        min_value=100,
        max_value=3000,
        value=600
    )

    pressure = st.number_input(
        "Pressure (bar)",
        min_value=1.0,
        max_value=40.0,
        value=10.0
    )

with col2:

    angle = st.selectbox(
        "Bend Angle",
        [22.5, 45, 90],
        index=2
    )

    allowable_bearing = st.number_input(
        "Allowable Bearing Pressure (kN/m²)",
        value=500
    )

if st.button("Design Support Block"):

    thrust = bend_thrust(
        diameter_mm=diameter,
        pressure_bar=pressure,
        angle_deg=angle
    )

    result = support_block_design(
        thrust_kn=thrust,
        allowable_bearing=allowable_bearing
    )

    st.subheader("Results")

    st.metric(
        "Hydraulic Thrust (kN)",
        result["thrust"]
    )

    st.metric(
        "Required Bearing Area (m²)",
        result["required_area"]
    )

    st.subheader("Recommended Concrete Support Block")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Length (m)",
        result["length"]
    )

    col2.metric(
        "Width (m)",
        result["width"]
    )

    col3.metric(
        "Height (m)",
        result["height"]
    )

    st.metric(
        "Concrete Volume (m³)",
        result["volume"]
    )

    st.success(
        "Recommended preliminary support block size generated."
    )

st.info("""
Assumptions:

• Support block transfers thrust into chamber slab.

• Chamber slab and surrounding structure resist the load.

• Preliminary sizing only.

• Final design should verify:
  - Slab reinforcement
  - Local bearing stress
  - Punching shear
  - Chamber stability
  - Soil bearing capacity
""")
