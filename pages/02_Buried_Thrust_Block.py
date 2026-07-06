import streamlit as st

from modules.soil import SOIL_DATABASE
from modules.designer import (
    bend_thrust,
    design_buried_block
)

st.title("🌍 Buried Thrust Block Designer")

dn = st.number_input(
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
    list(SOIL_DATABASE.keys())
)

design_basis = st.selectbox(
    "Design Basis",
    [
        "Preliminary",
        "Normal",
        "Critical"
    ]
)

sf_table = {
    "Preliminary": 1.25,
    "Normal": 1.5,
    "Critical": 2.0
}

if st.button("Design Block"):

    thrust = bend_thrust(
        dn,
        pressure,
        angle
    )

    sbc = SOIL_DATABASE[soil]["sbc"]

    result = design_buried_block(
        thrust,
        sbc,
        sf_table[design_basis]
    )

    st.success("Recommended Thrust Block")

    st.write(
        f"Hydraulic Thrust = {result['thrust']} kN"
    )

    st.write(
        f"Required Area = {result['area']} m²"
    )

    st.write(
        f"Length = {result['length']} m"
    )

    st.write(
        f"Width = {result['width']} m"
    )

    st.write(
        f"Depth = {result['depth']} m"
    )

    st.write(
        f"Concrete Volume = {result['volume']} m³"
    )
