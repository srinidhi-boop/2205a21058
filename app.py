import streamlit as st
st.title("student")

import streamlit as st
st.title("2205A21058-PS9")
st.header("Calculate the efficiency of DC shunt generator at various loads")

def Gen_Eff(v,cl,il,k,rsh,ra):
    ish=v/rsh
    ia=(k*il)-ish
    Cul=((ish*2)*rsh)+((ia*2)*ra)
    Eff=((k*v*il)/((k*v*il)+cl+Cul)*100)
    return Cul,Eff

col1,col2=st.columns(2)
with col1:
    v=st.number_input("V:in Volt", value=100)
    il=st.number_input("IL:in Amps", value=10.00)
    rsh=st.number_input("Rsh:in Ohms", value=10.00)
    ra=st.number_input("Ra:Ohms", value=10.00)
    cl=st.number_input("CL:Watts", value=100)
    k=st.number_input("Load",value=1)
    compute=st.button("compute")

with col2:
    with st.container(border=True):
        if compute:
            Cul,Eff=Gen_Eff(v,cl,il,k,rsh,ra)
            st.write(f"Eff={Eff:.2f} %")
            st.write(f"CUL={Cul:.2f} Watts")