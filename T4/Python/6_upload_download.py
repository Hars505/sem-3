import streamlit as st
import pandas as pd
st.set_page_config(page_title="Upload and Download",page_icon="🎓",layout="wide")
st.title("Upload and Download")
upload_file=st.file_uploader("Upload A csv file",type=["csv"])
download_file=st.button("Download File")
st.write("Click Below Button To See Data Of Marks")
if st.button("Data OF Marks"):
    data1=pd.DataFrame({"ROll_no.":[1,2,3,4],"Marks":[21,22,14,20]})
    st.dataframe(data1)
    csv=data1.to_csv(index=False).encode("UTF-8")
    st.download_button(label="Download CSV",data=csv,file_name="marks.csv")
