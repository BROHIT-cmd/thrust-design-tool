import streamlit as st

from modules.soil import SOIL_DATABASE
from modules.thrust import bend_thrust
from modules.buried import (
    required_area,
    block_size
)

st.title("Buried Thrust Block")

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

design = st.selectbox(
    "Design Basis",
    [
        "Preliminary",
        "Normal",
        "Critical"
    ]
)

sf_table = {
    "Preliminary": 1.25,
    "Normal": 1.50,
    "Critical": 2.00
}

if st.button("Calculate"):

    thrust = bend_thrust(
        dn,
        pressure,
        angle
    )

    sbc = SOIL_DATABASE[soil]["sbc"]

    sf = sf_table[design]

    area = required_area(
        thrust,
        sbc,
        sf
    )

    L, B = block_size(area)

    st.success(
        f"Thrust Force = {thrust:.2f} kN"
    )

    st.success(
        f"Required Area = {area:.2f} m²"
    )

    st.success(
        f"Recommended Block = {L:.2f}m × {B:.2f}m"
    )
