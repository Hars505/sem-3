import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
st.set_page_config(page_title="GRAPHS",page_icon="🎓",layout="centered")
st.title("GRAPHS")
st.subheader("Line chart")
x = np.arange(1,11)
y = np.random.randint(50,100,size=10)
# st.pyplot(x,y,marker='o')
# st.subheader("streamlit charts")
st.line_chart(y)
