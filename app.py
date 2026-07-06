import streamlit as st

st.title("Hello from Azure App Service 👋")
st.write("This Streamlit app is running in a Docker container on Azure!")

name = st.text_input("What's your name?")
if name:
    st.success(f"Nice to meet you, {name}!, hope you are doing well")
