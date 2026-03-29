import streamlit as st

st.set_page_config(layout="wide")

st.title("AASHTO 1993 Pavement Design")

a1 = st.number_input("a1", value=0.40)
m1 = st.number_input("m1", value=1.1)
d1 = st.number_input("d1 (cm)", value=20.3)

if st.button("Calculate"):
    d1 = d1 / 2.54
    SN = a1 * m1 * d1
    st.success(f"SN = {SN:.3f}")
