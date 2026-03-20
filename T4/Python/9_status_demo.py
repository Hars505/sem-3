import streamlit as st
import pandas as pd
import time
st.set_page_config(page_title="Status Demo",page_icon="🎓",layout="centered")
st.title("Status Demo")
if st.button("Start LongTask"):
    progress = st.progress(0)
    with st.spinner("Processing..."):
        for i in range(100):
            time.sleep(0.01)
            progress.progress(i+1)
    st.success("Task Completed")
st.warning("This is a Warning message")
st.error("This is a Error Message")
st.info("This is a info message")
