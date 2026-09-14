import streamlit as st

st.title("LAWS90286")

name = st.text_input("What is your name?")
age = st.number_input("What is your age?", min_value=0)

if st.button("Say hi"):
    st.write(f"Hello, {name}. I understand you are {age} years old.")
