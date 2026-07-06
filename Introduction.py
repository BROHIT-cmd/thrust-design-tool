import streamlit as st

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Pipeline Thrust Block Designer",
    page_icon="🏗",
    layout="wide"
)

# =====================================================
# HEADER
# =====================================================

col1, col2 = st.columns([6, 1])

with col1:
    st.title("🏗 Pipeline Thrust Block Designer")

with col2:
    try:
        st.image(
            "assets/logo.png",
            width=120
        )
    except:
        pass

st.caption(
    "Preliminary Engineering Design Tool for Pipeline Thrust block design"
)

# =====================================================
# WELCOME
# =====================================================

st.markdown("""
## Welcome

The **Pipeline Thrust Block Designer** has been developed to assist engineers in the
preliminary design and sizing of pipeline thrust block.

The application provides tools for:

✅ Buried Thrust Block Design

✅ SFA Chamber Thrust Block Design

✅ Hydraulic Thrust Calculations

✅ Water Hammer Consideration

✅ Soil Bearing Assessment

✅ Concrete Quantity Estimation

✅ Reinforcement Estimation

✅ Engineering Risk Assessment

✅ Design Report Generation

---

## Why Are Thrust Blocks Required?

When water flows through a pressurized pipeline and encounters a bend,
tee, reducer, valve or dead-end, an unbalanced force is generated.

This force is called:

### Hydraulic Thrust

If not restrained, hydraulic thrust may cause:

- Pipe movement
- Joint separation
- Leakage
- Structural damage
- Service interruption

Thrust blocks transfer these forces safely into:

- Surrounding soil (buried systems)

or

- Reinforced concrete structures (chambers)

---

## Available Modules

### 📚 Theory

Provides background information on:

- Hydraulic thrust
- Soil bearing capacity
- Water hammer
- Safety factors
- Concrete grades
- Design assumptions

---

### 📦 Buried Thrust Block Designer

Used for buried pipelines where thrust is resisted by the surrounding soil.

Typical applications:

- Water transmission mains
- Distribution networks
- Buried valve chambers
- Buried bends and fittings

Features:

- Soil selection
- Water hammer factors
- Safety factors
- Automatic block sizing
- Concrete quantity estimation

---

### 🏗 SFA Chamber Thrust Block Designer

Used when thrust forces are transferred into reinforced concrete structures.

Typical applications:

- Flow meter chambers
- Valve chambers
- Pump stations
- Treatment plants

Features:

- Concrete grade selection
- Chamber dimensions
- Reinforcement estimates
- Material quantities
- Design reporting

---

### ⚠️ Risk Assessment

Provides a preliminary engineering review of:

- Pressure risk
- Soil risk
- Water hammer risk
- Safety factor adequacy
- Block size requirements

and generates engineering recommendations.
""")

# =====================================================
# DESIGN PROCESS
# =====================================================

st.markdown("""
# 🔄 Detailed Design Process

The design of a thrust block is not simply a sizing exercise.

The objective is to safely transfer hydraulic forces generated inside
the pipeline into the surrounding soil or supporting concrete structure.

The following methodology is used within this application.

---

## Step 1 – Define Pipeline Characteristics

The designer enters the physical characteristics of the pipeline.

### Inputs Required

• Pipe Diameter (DN)

• Operating Pressure

• Bend Angle

• Soil Type

• Water Hammer Condition

• Design Classification

### Why?

Hydraulic thrust increases with:

✅ Larger pipe diameters

✅ Higher operating pressures

✅ Larger bend angles

Example:

DN1000 at 16 bar will produce significantly higher thrust than DN300 at 6 bar.

---

## Step 2 – Calculate Pipe Cross-Sectional Area

The internal area of the pipe is calculated.

Formula:

A = πD²/4

Where:

A = Pipe Area (m²)

D = Pipe Diameter (m)

### Example

DN800

Area ≈ 0.503 m²

The larger the area, the larger the hydraulic force.

---

## Step 3 – Calculate Hydraulic Thrust

When water changes direction at a bend, a force is developed.

This force attempts to push the fitting away from the pipeline.

Formula:

F = 2 × P × A × sin(θ/2)

Where:

F = Hydraulic Thrust

P = Internal Pressure

A = Pipe Area

θ = Bend Angle

### Example

Pressure = 16 bar

DN800

90° Bend

Hydraulic Thrust ≈ 1,140 kN

This force must be restrained.

---

## Step 4 – Evaluate Water Hammer Effects

Operating pressure is not always constant.

Pressure surges can occur due to:

• Rapid valve closure

• Pump trip

• Pump start

• Flow reversal

• Air release events

These surges increase the thrust force.

Water Hammer Factors:

None = 1.00

Mild Surge = 1.10

Moderate Surge = 1.20

Severe Surge = 1.30

### Example

Hydraulic Thrust = 1000 kN

Water Hammer Factor = 1.20

Adjusted Thrust

= 1200 kN

---

## Step 5 – Apply Safety Factor

Engineering designs must account for uncertainty.

Possible uncertainties include:

• Soil variability

• Construction tolerances

• Future operating changes

• Modelling assumptions

The safety factor increases the design load.

### Example

Adjusted Thrust = 1200 kN

Safety Factor = 2.0

Design Thrust

= 2400 kN

This value is used for design.

---

## Step 6 – Assess Ground Conditions

The thrust force must be resisted by soil.

The resistance of soil is represented by:

SBC = Safe Bearing Capacity

SBC is the maximum pressure the soil can safely resist.

Typical values:

Soft Clay = 50 kN/m²

Medium Clay = 100 kN/m²

Stiff Clay = 150 kN/m²

Dense Sand = 200 kN/m²

Gravel = 300 kN/m²

Rock = 1000 kN/m²

Higher SBC means smaller thrust blocks.

Lower SBC means larger thrust blocks.

---

## Step 7 – Calculate Required Bearing Area

The required contact area between the thrust block
and the soil is calculated.

Formula:

Required Area = Design Thrust / SBC

### Example

Design Thrust = 2400 kN

SBC = 150 kN/m²

Required Area

= 16 m²

The thrust block must provide at least this area.

---

## Step 8 – Determine Block Dimensions

The application calculates practical dimensions
for the thrust block.

Outputs:

• Length

• Width

• Depth

• Concrete Volume

• Reinforcement Estimate

Example:

4.0 m × 4.0 m × 1.2 m

Concrete = 19.2 m³

---

## Step 9 – Evaluate Engineering Risk

The Risk Assessment module reviews:

• Pressure Risk

• Soil Risk

• Water Hammer Risk

• Block Size Risk

• Safety Factor Adequacy

Outputs include:

✅ LOW RISK

⚠ MEDIUM RISK

🔶 HIGH RISK

🔴 CRITICAL RISK

Engineering recommendations are also generated.

---

## Step 10 – Generate Design Report

The final stage is documentation.

Reports include:

• Design Inputs

• Design Assumptions

• Hydraulic Calculations

• Soil Information

• Water Hammer Assumptions

• Recommended Block Dimensions

• Concrete Quantity

• Reinforcement Estimate

• Risk Assessment

• Engineering Notes

---

# Design Philosophy

The design philosophy adopted by this application is:

Hydraulic Force
↓
Design Thrust
↓
Soil Resistance
↓
Required Area
↓
Block Dimensions
↓
Risk Assessment

The objective is to ensure that all hydraulic forces generated within the pipeline are safely transferred into the surrounding ground without causing movement, joint failure, leakage, or structural damage.
""")
