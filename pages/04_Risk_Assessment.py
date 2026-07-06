import streamlit as st

st.title("Risk Assessment")

st.markdown("""
### Risk Categories

LOW
- FS > 2.0

MEDIUM
- FS = 1.5 to 2.0

HIGH
- FS = 1.0 to 1.5

EXTREME
- FS < 1.0

---

Potential Risks

✅ Pipe Movement

✅ Coupling Separation

✅ Chamber Sliding

✅ Structural Cracking

✅ Soil Settlement
""")
