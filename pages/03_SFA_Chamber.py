import streamlit as st

from modules.soil import SOIL_DATABASE
from modules.designer import (
    bend_thrust,
    design_chamber_support
)

st.title("🏗 SFA Chamber Support Designer")

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

if st.button("Design Support Block"):

    thrust = bend_thrust(
        dn,
        pressure,
        angle
    )

    mu = SOIL_DATABASE[soil]["mu"]

    support = design_chamber_support(
        thrust,
        mu
    )

    if support:

        st.success(
            "Recommended Support Block"
        )

        st.write(
            f"Hydraulic Thrust = {thrust:.2f} kN"
        )

        st.write(
            f"Length = {support['length']} m"
        )

        st.write(
            f"Width = {support['width']} m"
        )

        st.write(
            f"Height = {support['height']} m"
        )

        st.write(
            f"Concrete Volume = {support['volume']} m³"
        )

        st.write(
            f"Block Weight = {support['weight']} kN"
        )

        st.write(
            f"Sliding FOS = {support['sliding_fs']}"
        )

        st.success("SAFE")
