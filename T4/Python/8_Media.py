import streamlit as st
import pandas as pd
st.set_page_config(page_title="Media",page_icon="🎓",layout="centered")
st.title("Media {Image,Video,Audio}")
st.subheader("1. Image")
# "https://picsum.photos/600/300"
st.image("C:\\Users\\harsh\\Downloads\\Honet_badger.jpg",caption="Random Image",use_container_width=True)
st.subheader("2. Audio")
st.audio("C:\\Users\\harsh\\Downloads\\file_example_MP3_700KB.mp3")
st.subheader("3. Video")
st.video("https://www.w3schools.com/html/mov_bbb.mp4")
