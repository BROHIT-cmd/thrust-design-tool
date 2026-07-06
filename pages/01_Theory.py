import streamlit as st

st.title("Theory & Design Basis")

st.markdown("""
## What is Thrust?

Internal pressure acting on bends, tees,
reducers and dead ends creates an
unbalanced force known as thrust.

## Buried Pipe Load Path

Water Pressure

↓

Pipe Fitting

↓

Thrust Block

↓

Soil

---

## SFA Chamber Load Path

Water Pressure

↓

Pipe Bend

↓

Concrete Support

↓

Base Slab

↓

Soil

---

## Key Equations

### Bend Thrust

F = 2PA sin(θ/2)

### End Cap Thrust

F = PA

### Required Block Area

Area = (Thrust × Safety Factor) / SBC

---

The tool is intended for preliminary sizing.
Final design should be verified by Mechanical,
Civil and Geotechnical engineers.
""")
