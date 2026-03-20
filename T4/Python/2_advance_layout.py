import streamlit as st
st.set_page_config(page_title="ADVANCED",page_icon="🎄",layout="wide")
st.title("STUDENT PROFILE")
st.markdown("This is used to get demo of **sidebar**,**columns** and **expanders**")
st.sidebar.header("Profile Settings")
name=st.sidebar.text_input("Enter Student Name","Harshil")
Enroll=st.sidebar.text_input("Enter Enrollment Number")
Branch=st.sidebar.selectbox("Branch",["AIML","IT","CE","AIDS","CSEAI"])
st.sidebar.markdown("---")

col1,col2=st.columns([1,2])
with col1:
    st.subheader("Basic Details")
    st.write(f"Name of Student : {name}\n\n Enrollment Number of Student : {Enroll} \n\n Branch :{Branch}")
with col2:
    st.subheader("About")
    st.markdown("This is to Display Info Of Student")
with st.expander("Course Studied"):
    st.write("1. Python")
    st.write("2. JAVA")
