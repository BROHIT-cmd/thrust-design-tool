import streamlit as st

from modules.thrust import bend_thrust
from modules.chamber_support import design_support_block

st.title("🏗 SFA Chamber Support Designer")

# Inputs

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
    [22.5, 45, 90]
)

# Concrete Database

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
}

# Concrete Grade Selection

concrete_grade = st.selectbox(
    "Concrete Grade",
    [
        "C25/30",
        "C30/37",
        "C40/50"
    ],
    index=1
)

# Display Grade Information

grade_data = CONCRETE_DATA[concrete_grade]

st.info(
    f"""
Concrete Grade: {concrete_grade}

Characteristic Strength (fck): {grade_data['fck']} MPa

Assumed Bearing Capacity: {grade_data['bearing']} kN/m²

Description:
{grade_data['description']}
"""
)

# Help Section

with st.expander("📘 Concrete Grade Guide"):

    st.markdown("""
### C25/30

- 25 MPa cylinder strength
- 30 MPa cube strength

Typical Use:
- Small chambers
- Pipe supports
- General civil works

---

### C30/37 (Recommended)

- 30 MPa cylinder strength
- 37 MPa cube strength

Typical Use:
- Flow meter chambers
- Valve chambers
- Water treatment plants
- Pipe support blocks

---

### C40/50

- 40 MPa cylinder strength
- 50 MPa cube strength

Typical Use:
- Large pumping stations
- Heavy duty support blocks
- Critical infrastructure

---

✅ Recommended for most SFA chambers: **C30/37**
""")

# Design Button

if st.button("Design Support Block"):

    thrust = bend_thrust(
        diameter,
        pressure,
        angle
    )

    result = design_support_block(
        thrust,
        concrete_grade
    )

    st.subheader("Results")

    st.metric(
        "Hydraulic Thrust (kN)",
        round(thrust, 2)
    )


    st.metric(
        "Required Area (m²)",
        result["required_area"]
    )


    st.success(
        f"""
Recommended Support Block

Length = {result['length']} m

Width = {result['width']} m

Height = {result['height']} m
"""
    )

    st.write(
        f"Concrete Volume = {result['volume']} m³"
    )
