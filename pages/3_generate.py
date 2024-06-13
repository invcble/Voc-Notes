import streamlit as st
from Engine import split_audio, speech2text, LLM_call

st.title("Welcome to Voc-Notes!")
st.write("Hi Student!")

st.write("")
st.write("")
st.write("💿 Your Audio file is selected. 💿")
click_gen = st.button("1 - Start Generating Notes 📝")


st.write("========================================================")

if click_gen:
    st.write("Processing Audio to chunks...")
    split_audio()

    st.write("Converting Speech to text...")
    speech2text()

    st.write("Sending data to LLM to generate Note...")
    data = LLM_call()

    st.write("========================================================")
    st.page_link("app.py", label="Go back to Main menu 📃")
    
    st.markdown(data)