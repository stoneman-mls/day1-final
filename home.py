## these are libraries that are being imported
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# this is the title of the webpage
st.title("LAWS90286")

# here is some user input
name = st.text_input("What is your name?")
age = st.number_input("What is your age?", min_value=0)

# here is some logic to say hello
if st.button("Say hi"):
    st.write(f"Hello, {name}. I understand you are {age} years old.")


client = OpenAI()

if name is not None and name != "":
    
    response = client.responses.create(
        model="gpt-4o",
        input=f"Write a poem about {name}.",
    )

    st.write(response.output_text)
