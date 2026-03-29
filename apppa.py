import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# ------------------------
# Function AASHTO 1993
# ------------------------
def calc_SN_required(W18, Mr, So, ZR, deltaPSI):

    SN = 3.0

    for _ in range(20):
        term1 = ZR * So
        term2 = 9.36 * np.log10(SN + 1)
        term3 = (np.log10(deltaPSI/(4.2-1.5))) / (0.40 + (1094/(SN+1)**5.19))
        term4 = 2.32 * np.log10(Mr) - 8.07

        SN = 10 ** ((np.log10(W18) + term1 - term2 - term3 - term4)/9.36)

    return SN

# ------------------------
# Sidebar
# ------------------------
st.sidebar.title("AASHTO 1993")

road = st.sidebar.radio(
    "เลือกประเภทผิวทาง",
    ["Flexible Pavement","Rigid Pavement"]
)

W18 = st.sidebar.number_input("W18 (ESAL)", value=10000000.0, format="%.0f")
R = st.sidebar.slider("Reliability (%)",50,99,85)
So = st.sidebar.number_input("Standard Deviation",value=0.45)
deltaPSI = st.sidebar.number_input("ΔPSI",value=1.7)
Mr = st.sidebar.number_input("Mr (psi)",value=8000.0)

# ZR lookup
ZR_table = {
50:0,60:-0.253,70:-0.524,75:-0.674,
80:-0.841,85:-1.036,90:-1.282,
95:-1.645,98:-2.054,99:-2.327
}

ZR = ZR_table.get(R,-1.036)

# ------------------------
# Flexible
# ------------------------
if road == "Flexible Pavement":

    st.title("Flexible Pavement — AASHTO 1993")

    SN_req = calc_SN_required(W18, Mr, So, ZR, deltaPSI)

    st.subheader("Layer Properties")

    c1,c2,c3,c4,c5 = st.columns(5)

    with c1:
        a1=st.number_input("a1",0.0,1.0,0.40)
        m1=st.number_input("m1",0.0,2.0,1.0)
        d1=st.number_input("d1 cm",0.0,100.0,5.0)

    with c2:
        a2=st.number_input("a2",0.0,1.0,0.18)
        m2=st.number_input("m2",0.0,2.0,1.1)
        d2=st.number_input("d2 cm",0.0,100.0,20.0)

    with c3:
        a3=st.number_input("a3",0.0,1.0,0.13)
        m3=st.number_input("m3",0.0,2.0,1.1)
        d3=st.number_input("d3 cm",0.0,100.0,25.0)

    with c4:
        a4=st.number_input("a4",0.0,1.0,0.0)
        m4=st.number_input("m4",0.0,2.0,1.0)
        d4=st.number_input("d4 cm",0.0,100.0,0.0)

    with c5:
        a5=st.number_input("a5",0.0,1.0,0.0)
        m5=st.number_input("m5",0.0,2.0,1.0)
        d5=st.number_input("d5 cm",0.0,100.0,0.0)

    # SN cumulative
    SN1=a1*m1*(d1/2.54)
    SN2=SN1+a2*m2*(d2/2.54)
    SN3=SN2+a3*m3*(d3/2.54)
    SN4=SN3+a4*m4*(d4/2.54)
    SN5=SN4+a5*m5*(d5/2.54)

    total = d1+d2+d3+d4+d5

    col1,col2,col3,col4 = st.columns(4)

    col1.metric("SN Required",f"{SN_req:.3f}")
    col2.metric("SN Provided",f"{SN5:.3f}")
    col3.metric("Total Thickness",f"{total:.1f} cm")
    col4.metric("W18",f"{W18:,.0f}")

    if SN5 >= SN_req:
        st.success("ผ่าน")
    else:
        st.error("ไม่ผ่าน")

    st.subheader("Summary")

    st.table({
        "Layer":["AC","Base","Subbase","Layer4","Layer5"],
        "Thickness":[d1,d2,d3,d4,d5],
        "SN":[SN1,SN2,SN3,SN4,SN5]
    })

    st.subheader("Cross Section")

    fig,ax = plt.subplots()

    layers=[d1,d2,d3,d4,d5]
    colors=["black","gray","skyblue","orange","green"]

    y=0
    for i in range(len(layers)):
        ax.barh(0,layers[i],left=y)
        y+=layers[i]

    ax.set_yticks([])
    st.pyplot(fig)

# ------------------------
# Rigid
# ------------------------
if road == "Rigid Pavement":

    st.title("Rigid Pavement — AASHTO 1993")

    D = st.number_input("Slab Thickness cm",value=25.0)

    D_req = (np.log10(W18)+1)*5

    col1,col2 = st.columns(2)

    col1.metric("Required",f"{D_req:.1f}")
    col2.metric("Provided",f"{D:.1f}")

    if D >= D_req:
        st.success("ผ่าน")
    else:
        st.error("ไม่ผ่าน")
