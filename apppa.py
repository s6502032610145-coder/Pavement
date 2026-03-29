import streamlit as st

st.set_page_config(layout="wide")

st.title("ออกแบบผิวทางลาดยาง 5 ชั้น — AASHTO 1993")

# -------------------------------
# INPUT GLOBAL
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    esal = st.number_input("Design ESAL", value=900000000)

with col2:
    sn_required = st.number_input("SN Required", value=8.863)

st.divider()

st.subheader("Layer Properties")

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.markdown("### AC")
    a1 = st.number_input("a1", value=0.40)
    m1 = st.number_input("m1", value=1.1)
    d1 = st.number_input("d1 (cm)", value=20.3)

with c2:
    st.markdown("### Base")
    a2 = st.number_input("a2", value=0.18)
    m2 = st.number_input("m2", value=1.1)
    d2 = st.number_input("d2 (cm)", value=40.0)

with c3:
    st.markdown("### Subbase")
    a3 = st.number_input("a3", value=0.13)
    m3 = st.number_input("m3", value=1.1)
    d3 = st.number_input("d3 (cm)", value=40.0)

with c4:
    st.markdown("### Subgrade")
    a4 = st.number_input("a4", value=0.10)
    m4 = st.number_input("m4", value=1.0)
    d4 = st.number_input("d4 (cm)", value=10.0)

with c5:
    st.markdown("### Selected")
    a5 = st.number_input("a5", value=0.08)
    m5 = st.number_input("m5", value=1.0)
    d5 = st.number_input("d5 (cm)", value=5.0)

# -------------------------------
# CALCULATE
# -------------------------------
if st.button("Calculate"):

    # cm -> inch
    d1i = d1 / 2.54
    d2i = d2 / 2.54
    d3i = d3 / 2.54
    d4i = d4 / 2.54
    d5i = d5 / 2.54

    SN = (
        (a1*m1*d1i) +
        (a2*m2*d2i) +
        (a3*m3*d3i) +
        (a4*m4*d4i) +
        (a5*m5*d5i)
    )

    total_thickness = d1 + d2 + d3 + d4 + d5

    st.divider()

    c1, c2, c3 = st.columns(3)

    c1.metric("SN Provided", f"{SN:.3f}")
    c2.metric("SN Required", f"{sn_required}")
    c3.metric("Total Thickness", f"{total_thickness:.1f} cm")

    if SN >= sn_required:
        st.success("ผ่านการออกแบบ")
    else:
        st.error("ไม่ผ่าน ต้องเพิ่มความหนา")

    st.divider()

    st.subheader("Summary Table")

    st.table({
        "Layer": ["AC","Base","Subbase","Subgrade","Selected"],
        "a":[a1,a2,a3,a4,a5],
        "m":[m1,m2,m3,m4,m5],
        "Thickness(cm)":[d1,d2,d3,d4,d5]
    })
