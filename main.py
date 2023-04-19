import openai 
import streamlit as st
import Functions as F

openai.api_key = "YOUR_API_KEY"

st.title("ChatGPT Ask Anything")

st.header("ChatGPT - Enter the Question")    
question1 = st.text_input("")
if st.button("Get Answer"):
    answer1 = F.Main.Get_answer(question1)
    st.write(answer1)
