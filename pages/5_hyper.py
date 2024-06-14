import streamlit as st
from Engine import gen_hyper

st.title("Welcome to Voc-Notes!")
st.write("Hi Student!")

st.write("")
st.write("")
st.write("📉 You can generate .hyper file for data analysis using Tableau 📊")
click_hyper = st.button("Generate .hyper file 🛠️")
st.page_link("app.py", label="Go back to Main menu 📃")

st.write("========================================================")

if click_hyper:

    st.write(".hyper file generated.")
    print("Generating hyperfile")
    gen_hyper()