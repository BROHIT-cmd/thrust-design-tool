import streamlit as st

from modules.soil import SOIL_DATABASE
from modules.thrust import bend_thrust
from modules.buried import design_thrust_block

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="Buried Pipework Thrust Block Designer",
    page_icon="📦",
    layout="wide"
)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

col1, col2 = st.columns([6, 1])

with col1:
    st.title("📦 Buried Pipework Thrust Block Designer")

with col2:
    try:
        st.image(
            "assets/logo.png",
            width=120
        )
    except:
        pass

st.caption(
    "Preliminary design tool for buried pipeline thrust blocks"
)

# ---------------------------------------------------------
# INPUTS
# ---------------------------------------------------------

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
        value=10.0
    )

    angle = st.selectbox(
        "Bend Angle",
        [11.25, 22.5, 45, 90]
    )

with c2:

    soil = st.selectbox(
        "Soil Type",
        list(SOIL_DATABASE.keys()),
        index=2
    )

    design_class = st.selectbox(
        "Design Classification",
        [
            "Standard",
            "Critical",
            "Emergency Service"
        ]
    )

# ---------------------------------------------------------
# SOIL HELP
# ---------------------------------------------------------

with st.expander("📘 Soil Type Selection Guide"):
        
#SBC = Safe Bearing Capacity. It is the maximum pressure that the soil can safely withstand without excessive settlement or failure.
        
    st.markdown("""
### Soft Clay

**SBC = 50 kN/m²**

- Very weak soil
- High settlement risk
- Requires very large thrust blocks

---

### Medium Clay

**SBC = 100 kN/m²**

- Average soil condition
- Moderate bearing capacity

---

### Stiff Clay (Recommended)

**SBC = 150 kN/m²**

- Good bearing capacity
- Common for buried pipelines
- Recommended default selection

---

### Dense Sand

**SBC = 200 kN/m²**

- Good drainage
- Stable support conditions

---

### Gravel

**SBC = 300 kN/m²**

- High bearing capacity
- Excellent support conditions

---

### Rock

**SBC = 1000 kN/m²**

- Very high bearing capacity
- Smallest thrust blocks required

⚠ Always use geotechnical report data when available.
""")

# ---------------------------------------------------------
# SELECTED SOIL INFO
# ---------------------------------------------------------

st.info(
    f"""
Selected Soil : {soil}

Assumed Safe Bearing Capacity (SBC)

= {SOIL_DATABASE[soil]} kN/m²
"""
)

# ---------------------------------------------------------
# WATER HAMMER
# ---------------------------------------------------------

water_hammer_option = st.selectbox(
    "Water Hammer Condition",
    [
        "None",
        "Mild Surge (+10%)",
        "Moderate Surge (+20%)",
        "Severe Surge (+30%)"
    ],
    index=1
)

WATER_HAMMER_FACTOR = {
    "None": 1.00,
    "Mild Surge (+10%)": 1.10,
    "Moderate Surge (+20%)": 1.20,
    "Severe Surge (+30%)": 1.30
}

hammer_factor = WATER_HAMMER_FACTOR[
    water_hammer_option
]

# ---------------------------------------------------------
# DESIGN CLASS
# ---------------------------------------------------------

SAFETY_FACTORS = {
    "Standard": 1.50,
    "Critical": 2.00,
    "Emergency Service": 2.50
}

sf = SAFETY_FACTORS[
    design_class
]

st.info(
    f"""
Safety Factor = {sf}

Water Hammer Factor = {hammer_factor}
"""
)

# ---------------------------------------------------------
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

st.write(f"Selected Reinforcement Density: {STEEL_DENSITY} kg/m³")

# ---------------------------------------------------------
# DESIGN BUTTON
# ---------------------------------------------------------

if st.button(
    "🚀 Design Thrust Block",
    use_container_width=True
):

    # Hydraulic thrust

    thrust = bend_thrust(
        diameter,
        pressure,
        angle
    )

    # Design thrust

    design_thrust = (
        thrust
        * sf
        * hammer_factor
    )

    # Block sizing

    result = design_thrust_block(
        design_thrust,
        SOIL_DATABASE[soil],
        sf
    )

    # Material estimation

    concrete_volume = result["volume"]

    steel_weight = (
        concrete_volume
        * STEEL_DENSITY[steel_density]
    )

    # -----------------------------------------------------
    # DASHBOARD
    # -----------------------------------------------------

    st.header("Design Summary")

    d1, d2, d3 = st.columns(3)

    d1.metric(
        "Hydraulic Thrust",
        f"{thrust:.2f} kN"
    )

    d2.metric(
        "Design Thrust",
        f"{design_thrust:.2f} kN"
    )

    d3.metric(
        "Safety Factor",
        sf
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

    # -----------------------------------------------------
    # RECOMMENDED BLOCK
    # -----------------------------------------------------

    st.header("Recommended Thrust Block")

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
        "Depth",
        f"{result['depth']} m"
    )

    # -----------------------------------------------------
    # QUANTITY ESTIMATE
    # -----------------------------------------------------

    st.header("Quantity Estimate")

    st.success(
        f"""
Concrete Quantity

{concrete_volume:.2f} m³

Estimated Reinforcement

{steel_weight:.0f} kg
"""
    )

    # -----------------------------------------------------
    # REPORT
    # -----------------------------------------------------

    report = f"""
BURIED THRUST BLOCK DESIGN REPORT

Pipe Diameter : {diameter} mm

Pressure : {pressure} bar

Bend Angle : {angle}°

Soil Type : {soil}

Safety Factor : {sf}

Water Hammer Factor : {hammer_factor}

Hydraulic Thrust : {thrust:.2f} kN

Design Thrust : {design_thrust:.2f} kN

Required Area : {result['required_area']} m²

Recommended Block

Length : {result['length']} m

Width : {result['width']} m

Depth : {result['depth']} m

Concrete Volume : {concrete_volume:.2f} m³

Estimated Reinforcement : {steel_weight:.0f} kg
"""

    st.download_button(
        label="📄 Download Report",
        data=report,
        file_name="Buried_Thrust_Block_Report.txt",
        mime="text/plain"
    )

# ---------------------------------------------------------
# DISCLAIMER
# ---------------------------------------------------------

st.warning("""
This tool provides preliminary design sizing only.

Final design should verify:

• Geotechnical Investigation Results

• Soil Bearing Capacity

• Construction Constraints

• Hydrostatic Loading

• Water Hammer Analysis

• Project Standards

• Local Regulations

Always verify against project specifications.
""")
