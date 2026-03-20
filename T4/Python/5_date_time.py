import streamlit as st
from datetime import date,time
st.set_page_config(page_title="Date and Time",page_icon="🎓",layout="centered")
st.title("Date And Time")
exam_date=st.date_input("Select Date Of Exam",value=date.today())
exam_time=st.time_input("Selct Time of Exam",value=time(9,0))
