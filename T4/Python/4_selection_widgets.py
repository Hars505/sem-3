import streamlit as st
st.set_page_config(page_title="WIDGETS DEMO",page_icon="🎓",layout="centered")
st.title("WIDGETS DEMO")
subjects=st.selectbox("Subject",["Python","FSD-1","DE","PS"])
days=st.multiselect("Preferred Days",["MON","TUE","WED","THU","FRI","SAT","SUN"])
payment=st.radio("Payment Mode",["CASH","UPI","CARD","NET BANKING"],horizontal=True)
subscription=st.checkbox("IS SUBSCRIPTION IS TAKEN?",value=True)
