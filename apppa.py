# ======================================================
# RIGID PAVEMENT
# ======================================================
if road == "Rigid Pavement":

    st.title("Rigid Pavement — AASHTO 1993")

    st.subheader("Layer Properties")

    c1,c2,c3,c4,c5 = st.columns(5)

    with c1:
        a1 = st.number_input("a1", value=1.0, key="ra1")
        m1 = st.number_input("m1", value=1.0, key="rm1")
        d1 = st.number_input("D1 Concrete (cm)", value=25.0)

    with c2:
        a2 = st.number_input("a2", value=0.14, key="ra2")
        m2 = st.number_input("m2", value=1.0, key="rm2")
        d2 = st.number_input("D2 Base (cm)", value=10.0)

    with c3:
        a3 = st.number_input("a3", value=0.11, key="ra3")
        m3 = st.number_input("m3", value=1.0, key="rm3")
        d3 = st.number_input("D3 Subbase (cm)", value=15.0)

    with c4:
        a4 = st.number_input("a4", value=0.0, key="ra4")
        m4 = st.number_input("m4", value=1.0, key="rm4")
        d4 = st.number_input("D4 (cm)", value=0.0)

    with c5:
        a5 = st.number_input("a5", value=0.0, key="ra5")
        m5 = st.number_input("m5", value=1.0, key="rm5")
        d5 = st.number_input("D5 (cm)", value=0.0)

    # cumulative (เหมือน flexible)
    SN1 = a1*m1*(d1/2.54)
    SN2 = SN1 + a2*m2*(d2/2.54)
    SN3 = SN2 + a3*m3*(d3/2.54)
    SN4 = SN3 + a4*m4*(d4/2.54)
    SN5 = SN4 + a5*m5*(d5/2.54)

    total = d1+d2+d3+d4+d5

    # required (rigid simplified)
    SN_req = (np.log10(W18)+1)*3

    col1,col2,col3,col4 = st.columns(4)

    col1.markdown(f'<div class="metric m1">Required<br>{SN_req:.3f}</div>',unsafe_allow_html=True)
    col2.markdown(f'<div class="metric m2">Provided<br>{SN5:.3f}</div>',unsafe_allow_html=True)
    col3.markdown(f'<div class="metric m3">Total Thickness<br>{total:.1f} cm</div>',unsafe_allow_html=True)
    col4.markdown(f'<div class="metric m4">W18<br>{W18:,.0f}</div>',unsafe_allow_html=True)

    if SN5 >= SN_req:
        st.success("ผ่าน")
    else:
        st.error("ไม่ผ่าน")

    # ---------------- SUMMARY TABLE ----------------
    st.subheader("Summary")

    st.table({
        "Layer":["Concrete","Base","Subbase","Layer4","Layer5"],
        "Thickness (cm)":[d1,d2,d3,d4,d5],
        "SN":[SN1,SN2,SN3,SN4,SN5]
    })

    # ---------------- CROSS SECTION ----------------
    st.subheader("Cross Section")

    fig, ax = plt.subplots(figsize=(3,6))

    layers=[d1,d2,d3,d4,d5]
    names=["Concrete","Base","Subbase","Layer4","Layer5"]
    colors=["#dddddd","#bbbbbb","#87CEEB","#f4a261","#2a9d8f"]

    bottom=0
    for i in range(len(layers)):
        if layers[i] > 0:
            ax.bar(0,layers[i],bottom=bottom,color=colors[i])
            ax.text(
                0,
                bottom+layers[i]/2,
                f"{names[i]}\n{layers[i]} cm",
                ha="center",
                va="center"
            )
            bottom+=layers[i]

    ax.set_xticks([])
    ax.set_xlim(-1,1)

    st.pyplot(fig)
