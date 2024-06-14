import streamlit as st
from Engine import display_notes, download_note

st.title("Welcome to Voc-Notes!")
st.write("Hi Student!")

st.write("")
st.write("")
st.write("📂 You can view and download old notes here 📂")
click_gen = st.button("View all Notes 📝")
st.page_link("app.py", label="Go back to Main menu 📃")

if 'view' not in st.session_state:
    st.session_state.view = False

if 'download' not in st.session_state:
    st.session_state.download = False
    
st.write("========================================================")

if click_gen:
    st.session_state.view = True

if st.session_state.view:
    st.write("Below are your saved notes from the database...")
    notes_list = display_notes()
    for note in notes_list:
        st.write(note)
    
    st.write("========================================================")

    file2download = st.text_input("To download a Note, copy its name and paste here..")
    if file2download:
        download_note(file2download)