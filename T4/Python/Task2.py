import streamlit as st
import pandas as pd
st.set_page_config(page_title="STUDENT FEEDBACK FORM",page_icon="🎓",layout="wide")
st.title("STUDENT FEEDBACK")
Name=st.text_input("Enter Your Name")
Enroll=st.text_input("Enter Your Enrollment Number")
Subject=st.text_input("Enter Subject")
rating=st.slider("Five Rating On Quality Of Teaching",min_value=0,max_value=10,value=5)
Pref=st.radio("Mode OF Study Preference ",["Online","Offline","Hybrid"],horizontal=True)
Feedback=st.text_area("Enter Your Thoughts On FeedBack")
data1=pd.DataFrame({"Name":[Name],"Enrollment Number":[Enroll],"Quality of Teaching":[rating],"Preference For Mode Of Study":[Pref],"Feedback Thoughts":[Feedback]})
st.write("Click Below Button To See Data Of Marks")
if st.button("Data OF Marks"):
    st.dataframe(data1)
    csv=data1.to_csv(index=False).encode("UTF-8")
    st.download_button(label="Download CSV",data=csv,file_name="data1.csv")
