import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Force load env
load_dotenv()



model = ChatGoogleGenerativeAI(
    model="models/gemini-flash-latest",

)

st.header("Research Tool")

user_input = st.text_area("Enter your prompts")

if st.button("Summarize"):
    result = model.invoke(user_input)
    st.write(result.content)
