import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# -----------------------
# SIDEBAR
# -----------------------
st.sidebar.title("AASHTO 1993")

road_type = st.sidebar.radio(
    "เลือกประเภทผิวทาง",
    ["Flexible Pavement","Rigid Pavement"]
)

st.sidebar.subheader("Traffic")

W18 = st.sidebar.number_input("W18 (ESAL)", value=900000000.0, format="%.0f")
R = st.sidebar.slider("Reliability (%)", 50, 99, 90)
So = st.sidebar.number_input("Standard Deviation", value=0.45)
deltaPSI = st.sidebar.number_input("ΔPSI", value=1.7)

st.sidebar.subheader("Subgrade")

Mr = st.sidebar.number_input("Mr (psi)", value=8000.0)

# -----------------------
# FLEXIBLE
# -----------------------
if road_type == "Flexible Pavement":

    st.title("Flexible Pavement — AASHTO 1993")

    # -----------------------
    # SN Required Calculation
    # -----------------------
    ZR = -1.282  # approx for 90%
    SN_req = (
        (np.log10(W18) - ZR*So + 2.32*np.log10(Mr) - 8.07)
        /
        (0.4 + (1094/(SN_req if 'SN_req' in locals() else 5.0)**5.19))
    ) if W18>0 else 0

    # -----------------------
    # LAYER INPUT
    # -----------------------
    st.subheader("Layer Properties")

    c1,c2,c3,c4,c5 = st.columns(5)

    with c1:
        a1=st.number_input("a1",value=0.40)
        m1=st.number_input("m1",value=1.1)
        d1=st.number_input("d1 cm",value=20.0)

    with c2:
        a2=st.number_input("a2",value=0.18)
        m2=st.number_input("m2",value=1.1)
        d2=st.number_input("d2 cm",value=40.0)

    with c3:
        a3=st.number_input("a3",value=0.13)
        m3=st.number_input("m3",value=1.1)
        d3=st.number_input("d3 cm",value=40.0)

    with c4:
        a4=st.number_input("a4",value=0.10)
        m4=st.number_input("m4",value=1.0)
        d4=st.number_input("d4 cm",value=10.0)

    with c5:
        a5=st.number_input("a5",value=0.08)
        m5=st.number_input("m5",value=1.0)
        d5=st.number_input("d5 cm",value=5.0)

    # -----------------------
    # CALC
    # -----------------------
    SN1=a1*m1*(d1/2.54)
    SN2=SN1 + a2*m2*(d2/2.54)
    SN3=SN2 + a3*m3*(d3/2.54)
    SN4=SN3 + a4*m4*(d4/2.54)
    SN5=SN4 + a5*m5*(d5/2.54)

    total = d1+d2+d3+d4+d5

    col1,col2,col3,col4 = st.columns(4)

    col1.metric("SN Required",f"{SN_req:.3f}")
    col2.metric("SN Provided",f"{SN5:.3f}")
    col3.metric("Total Thickness",f"{total:.1f} cm")
    col4.metric("W18",f"{W18:,.0f}")

    if SN5>=SN_req:
        st.success("ผ่าน")
    else:
        st.error("ไม่ผ่าน")

    # -----------------------
    # TABLE
    # -----------------------
    st.subheader("Summary")

    st.table({
        "Layer":["AC","Base","Subbase","Subgrade","Selected"],
        "Thickness":[d1,d2,d3,d4,d5],
        "SN":[SN1,SN2,SN3,SN4,SN5]
    })

    # -----------------------
    # SECTION
    # -----------------------
    st.subheader("Cross Section")

    fig,ax=plt.subplots()

    layers=[d1,d2,d3,d4,d5]
    colors=["black","gray","skyblue","orange","green"]

    y=0
    for i in range(len(layers)):
        ax.barh(0,layers[i],left=y)
        y+=layers[i]

    ax.set_yticks([])
    st.pyplot(fig)

    # -----------------------
    # SENSITIVITY
    # -----------------------
    st.subheader("Sensitivity")

    ESAL_range=np.linspace(W18*0.1,W18*2,20)
    SN_curve=np.log10(ESAL_range)

    fig2,ax2=plt.subplots()
    ax2.plot(ESAL_range,SN_curve)
    ax2.set_title("Sensitivity ESAL vs SN")

    st.pyplot(fig2)

# -----------------------
# RIGID
# -----------------------
if road_type == "Rigid Pavement":

    st.title("Rigid Pavement — AASHTO 1993")

    D = st.number_input("Slab Thickness cm",value=25.0)

    D_req=(np.log10(W18)+1)*5

    col1,col2=st.columns(2)

    col1.metric("Required",f"{D_req:.1f}")
    col2.metric("Provided",f"{D:.1f}")

    if D>=D_req:
        st.success("ผ่าน")
    else:
        st.error("ไม่ผ่าน")
