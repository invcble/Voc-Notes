import streamlit as st
from Engine import start_recording, stop_recording
import time

st.title("Welcome to Voc-Notes!")
st.write("Hi Student!")

st.write("🎙️ You chose to record the Audio! 🎙️")
click_start = st.button("1 - Start Recording ⏺️")
click_stop = st.button("2 - Stop Recording ⏸️")


if "start" not in st.session_state:
    st.session_state.start = False

if "stop" not in st.session_state:
    st.session_state.stop = False


if click_start:
    st.session_state.start = True
    st.session_state.stop = False

if click_stop:
    st.session_state.start = False
    st.session_state.stop = True

if st.session_state.start:
    st.write("Recording started...")
    start_recording()

if st.session_state.stop:
    st.write("Recording stopped...")
    stop_recording()
    st.write("Recording successfully saved.")

st.write("========================================================")

st.page_link("pages\\3_generate.py", label="3 - Generate Notes 📄")