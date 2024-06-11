import streamlit as st
from Engine import start_recording, stop_recording

st.title("Welcome to Voc-Notes!")
st.write("'''Hi Student! Meet your AI-powered Lecture Note maker. 🤖'''")

st.write("What do you want to do?")
# # st.download_button()

st.page_link("pages\\1_record.py", label="Record Audio", icon='🎙️')
st.page_link("pages\\2_upload.py", label="Upload Audio", icon='📤')