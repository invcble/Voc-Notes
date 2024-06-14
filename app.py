import streamlit as st

st.title("Welcome to Voc-Notes!")
st.write("'''Hi Student! Meet your new free-to-use AI-powered Lecture Note maker. 🤖'''")

st.write("")
st.write("")
st.write("What do you want to do?")
# # st.download_button()

st.page_link("pages\\1_record.py", label="Record Audio & Generate Note.", icon='🎙️')

st.page_link("pages\\2_upload.py", label="Upload Audio & Generate Note.", icon='📤')

st.page_link("pages\\4_database.py", label="View and Download saved Notes.", icon='💾')

st.page_link("pages\\5_hyper.py", label="Generate Hyper file for Tableau.", icon='📈')