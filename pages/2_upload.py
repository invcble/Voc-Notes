import streamlit as st
from Engine import upload_recording
import time

st.title("Welcome to Voc-Notes!")
st.write("Hi Student!")

st.write("")
st.write("")
st.write("📤 You chose to upload the Audio! 📤")
click_upload = st.button("1 - Start Uploading ⬆️")


if "upload" not in st.session_state:
    st.session_state.upload = False

if "stop" not in st.session_state:
    st.session_state.stop = False


if click_upload:
    st.session_state.upload = True

if st.session_state.upload:
    st.write("Please paste the path to the audio file below...")
    answer = st.text_input("Copy as Path and paste.")
    if answer != '':
        if answer[1:-1].endswith('.mp3'):
            st.write("Uploading file...")
            upload_recording(answer[1:-1])

            time.sleep(1)
            st.write("File uploaded.")
        else:
            st.write("File is not a .mp3!")

st.write("========================================================")

st.page_link("pages\\3_generate.py", label="2 - Generate Notes 📄")