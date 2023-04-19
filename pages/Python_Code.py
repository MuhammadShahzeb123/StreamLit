import openai 
import streamlit as st
from Functions import Main
openai.api_key = "YOUR_API_KEY"

st.title("ChatGPT Ask Anything")

st.header("ChatGPT - Enter the Problem to solve")    
question1 = st.text_input("")



if st.button("Get Code"):
    answer1 = Main.Python_Code(question1)
    query = answer1
    st.write(f"```\n{answer1}\n```")
    Main.PythonCodeChecker(query)

