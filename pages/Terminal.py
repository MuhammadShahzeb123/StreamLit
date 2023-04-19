import streamlit as st
import os
from Functions import Main


st.title("Terminal")

st.header("Welcome to the Terminal")
command = st.text_input("")

if st.button("Run"):
    Output = os.system(command)
    st.write(Output)