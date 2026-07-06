import streamlit as st

from modules.soil import SOIL_DATABASE
from modules.thrust import bend_thrust
from modules.chamber import (
    concrete_volume,
    concrete_weight,
    sliding_fs
)
from modules.risk import risk_rating

st.title("SFA Chamber Support Design")

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

length = st.number_input(
    "Block Length (m)",
    value=1.5
)

width = st.number_input(
    "Block Width (m)",
    value=1.5
)

height = st.number_input(
    "Block Height (m)",
    value=1.0
)

if st.button("Check Design"):

    thrust = bend_thrust(
        dn,
        pressure,
        angle
    )

    volume = concrete_volume(
        length,
        width,
        height
    )

    weight = concrete_weight(
        volume
    )

    mu = SOIL_DATABASE[soil]["mu"]

    fs = sliding_fs(
        thrust,
        weight,
        mu
    )

    risk = risk_rating(fs)

    st.subheader("Results")

    st.write(f"Hydraulic Thrust : {thrust:.2f} kN")
    st.write(f"Concrete Volume : {volume:.2f} m³")
    st.write(f"Block Weight : {weight:.2f} kN")
    st.write(f"Sliding FOS : {fs:.2f}")
    st.write(f"Risk Level : {risk}")
