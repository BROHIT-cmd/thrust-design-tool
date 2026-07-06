# pages/01_Theory.py

import streamlit as st

st.set_page_config(
    page_title="Theory & Design Basis",
    layout="wide"
)

st.title("📚 Theory & Design Basis")
col1, col2 = st.columns([6, 1])

with col1:
    st.title("📚 Theory & Design Basis")

with col2:
    try:
        st.image(
            "assets/logo.png",
            width=120
        )
    except:
        pass

st.markdown("""

# 1. Introduction

Pressurized water pipelines are subjected to internal pressure at all times.

For a straight pipeline, the pressure forces acting in opposite directions
are equal and therefore cancel each other.

As a result:

**Net Force = 0**

No thrust force is generated.

However, when the pipeline changes direction, size, or flow path,
the pressure forces become unbalanced and create a resultant force
known as **Hydraulic Thrust**.

---

# 2. Locations Where Thrust Occurs

Hydraulic thrust develops at:

- Bends
- Tees
- Wyes
- Reducers
- Dead Ends
- Blind Flanges
- Closed Valves
- Flow Meter Assemblies
- Pump Headers

If these forces are not restrained, they may cause:

- Joint Separation
- Pipe Movement
- Leakage
- Structural Damage
- Equipment Misalignment

---

# 3. Pressure Forces in a Straight Pipe

Consider a straight pipe:

P × A  ←────────────→  P × A

Where:

P = Internal Pressure

A = Internal Pipe Area

Since the forces are equal and opposite:

Resultant Force = 0

Therefore no thrust force develops.

---

# 4. Why Thrust Occurs at a Bend

When water passes through a bend:

          ↑
          │
          │
        ╭─╯
        │
────────╯

Pressure acts on both legs of the bend.

The forces are no longer balanced.

A resultant force develops that attempts to push the bend away from
the corner.

This force is called:

HYDRAULIC THRUST

---

# 5. Pipe Internal Area

The internal pipe area is:

A = πD² / 4

Where:

A = Internal Area (m²)

D = Internal Diameter (m)

This area is used in all thrust calculations.

---

# 6. Bend Thrust Equation

For any bend:

F = 2PA sin(θ/2)

Where:

F = Thrust Force

P = Internal Pressure

A = Internal Pipe Area

θ = Bend Angle

---

# 7. Typical Bend Multipliers

22.5° Bend

F = 0.39PA

45° Bend

F = 0.77PA

90° Bend

F = 1.414PA

Larger bend angles generate larger thrust forces.

---

# 8. Dead-End Force

For a blind flange, end cap, or closed valve:

F = PA

This force acts along the pipe centerline and attempts to push the
pipe away from the closure.

Dead-end conditions often generate some of the highest thrust forces
in a pipeline.

---

# 9. Example

DN600 Pipeline

Pressure = 10 bar

Internal Diameter = 600 mm

Area:

A = π × 0.6² / 4

A = 0.283 m²

Dead-End Force:

F = PA

F = 1000 × 0.283

F = 283 kN

Therefore:

283 kN of force must be restrained.

---

# 10. Buried Pipeline Thrust Block Concept

In buried pipelines, thrust is generally resisted by a concrete
thrust block bearing against undisturbed soil.

Load Path:

Water Pressure

↓


Pipe Fitting

↓


Concrete Thrust Block

↓


Undisturbed Soil

The block transfers hydraulic force to the surrounding soil.

The soil ultimately provides the resistance.

---

# 11. Soil Resistance

When thrust force is transferred into the soil:

Hydraulic Thrust →

██████████████

← Soil Reaction

The soil produces an equal and opposite reaction.

For safety:

Soil Resistance ≥ Hydraulic Thrust

---

# 12. Safe Bearing Capacity (SBC)

Safe Bearing Capacity is the maximum pressure the soil can safely
withstand.

Typical values:

Soft Clay = 50 kN/m²

Medium Clay = 100 kN/m²

Stiff Clay = 150 kN/m²

Dense Sand = 200 kN/m²

Gravel = 300 kN/m²

Rock = 1000 kN/m²

Whenever available, actual geotechnical investigation data should
be used instead of assumed values.

---

# 13. Required Thrust Block Area

The required thrust block bearing area is:

Area = (Thrust × Safety Factor) / SBC

Where:

Area = Required Soil Bearing Area

Thrust = Hydraulic Force

Safety Factor = Design Factor

SBC = Allowable Soil Pressure

Poor soil conditions require larger thrust blocks.

---

# 14. Safety Factor

Safety factors account for:

- Soil uncertainty
- Construction tolerances
- Pressure surges
- Water hammer
- Material variability
- Long-term performance

Typical values:

Preliminary Design = 1.25

Normal Design = 1.50

Critical Infrastructure = 2.00

For most water infrastructure projects, FS = 1.5 is commonly used.

---

# 15. SFA / Valve Chamber Systems

In valve chambers or SFA chambers, forces are often transferred to
concrete supports instead of conventional buried thrust blocks.

Typical components:

- Butterfly Valve
- Flow Meter
- Flexible Coupling
- Dismantling Joint
- Bend
- Flanged Spool Pieces

The generated thrust must still be restrained.

---

# 16. SFA Chamber Load Transfer Mechanism

Typical load path:

Water Pressure

↓

90° Bend

↓

Pipe Barrel

↓

Concrete Support

↓

Base Slab

↓

Foundation Soil

The support block transfers the force into the chamber slab.

The chamber slab transfers the force into the soil.

The entire structure participates in resisting the hydraulic load.

---

# 17. Chamber Stability Checks

Unlike buried thrust blocks, chamber supports require additional
structural checks.

These include:

- Sliding
- Overturning
- Bearing Pressure
- Concrete Bearing Stress

---

# 18. Sliding Check

The chamber must not move horizontally.

The factor of safety against sliding is:

FS = Resisting Force / Driving Force

Where:

Driving Force = Hydraulic Thrust

Resisting forces may include:

- Concrete Weight
- Base Slab Weight
- Soil Friction
- Passive Soil Resistance

Target:

FS > 1.5

---

# 19. Overturning Check

Hydraulic thrust can create overturning moments.

The structure must remain stable.

Overturning Factor of Safety:

FS = Resisting Moment / Overturning Moment

Target:

FS > 2.0

---

# 20. Bearing Pressure Check

The pressure on the supporting soil should be less than the allowable SBC.

Bearing Pressure:

q = Load / Area

Requirement:

q < SBC

If this condition is not satisfied:

- Settlement may occur
- Pipe alignment may be affected
- Structural cracking may develop

---

# 21. Risk Assessment Philosophy

Risk assessment helps us understand:

1. How likely the system is to fail
2. What happens if it fails

The tool uses both of these to determine the overall risk level.

---

# Why Risk Assessment is Important

Even if a design passes the calculations, failure can still occur due to:

- Poor soil conditions
- Construction errors
- Higher operating pressure
- Water hammer
- Settlement
- Incorrect installation

Therefore risk should always be considered.

---

# Common Risks

## Buried Pipeline

Possible problems:

- Thrust block too small
- Pipe movement
- Joint separation
- Leakage

---

## Valve Chamber / SFA Chamber

Possible problems:

- Support block movement
- Chamber sliding
- Chamber cracking
- Flow meter misalignment
- Valve damage

---

# Risk Levels

## LOW

✅ Design is safe

The support has enough capacity.

No major concerns.

Example:

Factor of Safety > 2.0

---

## MEDIUM

⚠ Design is acceptable

However, engineering review is recommended.

Example:

Factor of Safety between 1.5 and 2.0

---

## HIGH

⚠ Design may not be reliable

Changes should be considered.

Example:

Factor of Safety between 1.0 and 1.5

Possible consequences:

- Pipe movement
- Leakage
- Structural damage

---

## EXTREME

❌ Design is unsafe

Redesign is required.

Example:

Factor of Safety less than 1.0

Failure is likely.

---

# Consequences of Failure

If the thrust restraint system fails, the following may happen:

### Mechanical Problems

- Pipe movement
- Coupling pull-out
- Flange leakage
- Valve damage

### Structural Problems

- Cracked concrete
- Chamber movement
- Slab damage

### Operational Problems

- Water leakage
- Service interruption
- Emergency repairs

---

# How Risk Can Be Reduced

The risk can be reduced by:

- Increasing thrust block size
- Increasing support size
- Increasing foundation area
- Improving soil conditions
- Using restrained joints
- Increasing safety factor

---

# Final Risk Decision

🟢 LOW

Safe for normal operation.

---

🟡 MEDIUM

Acceptable but review recommended.

---

🟠 HIGH

Design improvement recommended.

---

🔴 EXTREME

Design is not acceptable and must be redesigned.


# 22. Potential Failure Modes

Mechanical Failures

- Pipe Movement
- Joint Separation
- Coupling Pull-Out
- Flange Leakage

Civil Failures

- Chamber Sliding
- Wall Cracking
- Base Slab Movement
- Structural Instability

Geotechnical Failures

- Excess Bearing Pressure
- Settlement
- Differential Settlement

Operational Impacts

- Water Leakage
- Service Interruption
- Equipment Damage
- Increased Maintenance Costs

---

# 23. Design Basis Used in This Tool

Buried Pipeline Module:

- Hydraulic Thrust Calculation
- Soil Resistance Method
- Thrust Block Sizing

SFA Chamber Module:

- Hydraulic Thrust Calculation
- Concrete Support Design
- Sliding Assessment
- Bearing Assessment
- Risk Evaluation

---

# 24. Disclaimer

This tool is intended for: Preliminary design only. Results should be verified against project specifications, geotechnical data, and applicable standards before construction.

✅ Preliminary Design

✅ Concept Design

✅ Budget Estimating

✅ Design Review

✅ Engineering Verification

Final designs must always be reviewed by qualified Mechanical, Civil and Geotechnical Engineers and verified against project specifications and local standards.
""")
