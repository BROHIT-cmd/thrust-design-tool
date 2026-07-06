import streamlit as st

from modules.soil import SOIL_DATABASE
from modules.thrust import bend_thrust
from modules.buried import design_thrust_block

st.title("🌍 Buried Thrust Block Designer")

diameter = st.number_input(
    "Pipe Diameter (mm)",
    100,
    3000,
    600
)

pressure = st.number_input(
    "Pressure (bar)",
    1.0,
    40.0,
    10.0
)

angle = st.selectbox(
    "Bend Angle",
    [22.5, 45, 90]
)

soil = st.selectbox(
    "Soil Type",
    list(
        SOIL_DATABASE.keys()
    )
)

sf = st.selectbox(
    "Safety Factor",
    [1.25, 1.5, 2.0],
    index=1
)

if st.button("Design Thrust Block"):

    thrust = bend_thrust(
        diameter,
        pressure,
        angle
    )

    result = design_thrust_block(
        thrust,
        SOIL_DATABASE[soil],
        sf
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
        Recommended Block

        {result['length']} m ×
        {result['width']} m ×
        {result['depth']} m
        """
    )

    st.write(
        "Concrete Volume:",
        result["volume"],
        "m³"
    )
