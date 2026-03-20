import streamlit as st
import pandas as pd
st.set_page_config(page_title="Display Data",page_icon="🎓",layout="centered")
st.title("Display Data ,Table ,Json")
df=pd.DataFrame({"Name":['A',"B","C","D"],"Marks":[7,20,24,16],"Result":[False,True,True,True]})
st.subheader("1.Data Frame")
st.dataframe(df)
st.subheader("2. Table")
st.table(df)
st.subheader("3. Json")
st.json({"Name":['A',"B","C","D"],"Marks":[7,20,24,16],"Result":[False,True,True,True]})
