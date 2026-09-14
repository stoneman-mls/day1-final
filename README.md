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