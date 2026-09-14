# day1-final

## SETUP
1. create virtual environment
> python -m venv .venv
2. activate virtual environment
> source .venv/bin/activate
3. install streamlit
> pip install streamlit
4. create a python file
> touch home.py
5. run streamlit, using the python file from step 4 as the entry point
> streamlit run home.py
6. edit the python file to add functionality
> import streamlit as st
> st.title("LAWS90286")

## To save code to GitHub

1. Navigate to source control on LHS of screen
2. Click to "stage all changes"
3. Enter a commit message
4. Click commit
5. Sync changes

## To add things that are private that don't go to GitHub
1. Create .env file
2. Add secrets to the .env file
3. Access those secrets in code
> OPENAI_API_KEY="<insert>"
4. Create a .gitignore file and add the .env to it

## To use the OpenAI API to do things
1. Access the secrets (including the API Key) from .env
> pip install python-dotenv
> from dotenv import load_dotenv
> add load_dotenv() in your code file

2. pip install the OpenAI client
> pip install openai

3. Use the OpenAI client in your code
> from openai import OpenAI

4. Setup the OpenAI client and include the basic API call
> client = OpenAI()
> response = client.responses.create(
    model="gpt-4o",
    input=f"Write a poem about {name}.",
)
> st.write(response.output_text)