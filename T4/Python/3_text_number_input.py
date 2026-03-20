import streamlit as st
st.set_page_config(page_title="TEXT INPUT",page_icon="🎄",layout="centered")
st.title("Text And Number INput Methods")
name=st.text_input("Enter Your Name")
comments=st.text_area("Enter Any Commments")
st.write("Live Output")
if name:
    st.write(f"Name : {name}")
    st.markdown("---")
if comments:
    st.write(f"Comment : {comments}")
age=st.number_input("Enter Your Age",min_value=15,max_value=60,value=18)
ratings=st.slider("Enter Ratings(0-10)",min_value=0,max_value=10,value=5)
