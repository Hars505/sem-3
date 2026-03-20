import streamlit as st
st.set_page_config(page_title="DEPARTMENT OF LJ",page_icon="🎓",layout="wide")
st.title("Department Home Page")
st.header("LJ Department")
st.subheader("Details of Department")
st.markdown("Instructions Are As Follow : ")
Department=st.sidebar.selectbox("Department",["CSE","IT","AI-ML"])
Year=st.sidebar.selectbox("Year",["1st","2nd","3rd","4th"])
col1,col2=st.columns([1,2])
with col1:
    st.subheader("Basic Department Status")
    st.write(f"Department : {Department}")
    st.write(f"Year : {Year}")
with col2:
    st.subheader("Short Description")
    st.markdown("Every Student Must have Attendance above 75% ")
with st.expander("Strong Points"):
    st.write("1. Key Achievement")
    st.write("2. Rule Obeying")
