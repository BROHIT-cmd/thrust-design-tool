import streamlit as st

from modules.thrust import bend_thrust
from modules.chamber_support import (
    design_support_block
)

st.title(
    "🏗 SFA Chamber Support Designer"
)

diameter = st.number_input(
    "Pipe Diameter (mm)",
    100,
    3000,
    800
)

pressure = st.number_input(
    "Pressure (bar)",
    1.0,
    40.0,
    16.0
)

angle = st.selectbox(
    "Bend Angle",
    [22.5, 45, 90]
)

CONCRETE_DATA = {
    "C25/30": {
        "fck": 25,
        "bearing": 500,
        "description": "General purpose concrete for light to moderate loads."
    },
    "C30/37": {
        "fck": 30,
        "bearing": 600,
        "description": "Recommended for most flow meter and valve chambers."
    },
    "C40/50": {
        "fck": 40,
        "bearing": 800,
        "description": "Heavy-duty concrete for critical infrastructure and high loads."
    }

    concrete_grade = st.selectbox(
    "Concrete Grade",
    [
        "C25/30",
        "C30/37",
        "C40/50"
    ],
    index=1
)

if st.button(
    "Design Support Block"
):

    thrust = bend_thrust(
        diameter,
        pressure,
        angle
    )

    result = design_support_block(
        thrust,
        concrete_grade
    )

    st.metric(
        "Hydraulic Thrust (kN)",
        round(thrust, 2)
    )

    st.metric(
        "Required Area (m²)",
        result["area"]
    )

    st.success(
        f"""
        Recommended Support Block

        {result['length']} m ×
        {result['width']} m ×
        {result['height']} m
        """
    )

    st.write(
        "Volume:",
        result["volume"],
        "m³"
    )
