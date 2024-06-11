import streamlit as st

st.title("Welcome to Voc-Notes!")
st.write("'''Hi Student! Meet your new free-to-use AI-powered Lecture Note maker. 🤖'''")

st.write("")
st.write("")
st.write("What do you want to do?")
# # st.download_button()

st.page_link("pages\\1_record.py", label="Record Audio", icon='🎙️')

st.page_link("pages\\2_upload.py", label="Upload Audio", icon='📤')