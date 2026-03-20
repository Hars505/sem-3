import streamlit as st
st.set_page_config(page_title=" BASICS ",page_icon="🎄",layout="wide")
st.header("Hello World !! 🎄")
st.title("STREAMLIT")
st.subheader("This is a sub Header")
st.text("This is _Text Mode_ 62 262")
st.write("This is _Write Mode_ 61515")
code='''
def add(x,y):
    return x+y
Z=add(3,5)
print(z)
'''
st.code(code,language="python")
