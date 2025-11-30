import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import groq

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["LANGCHAIN_API_KEY"]=st.secrets["LANGCHAIN_API_KEY"]
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Q&A Chatbot -Groq"

## Prompt Template
prompt=ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant, answer the user's question clearly and professionally."),
    ("human","Question : {Question}")
])

def generate_response(Question,api_key,llm,temperature,max_tokens):

    if not api_key:
        return "⚠ Please Enter your Groq API key"
    try:           
        groq.api_key=api_key
        llm=ChatGroq(model=llm,temperature=temperature,max_tokens=max_tokens,api_key=api_key)
        output_parser=StrOutputParser()
        chain=prompt|llm|output_parser
        answer=chain.invoke({'Question': Question})
        return answer
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Title of App
st.title("Q&A Chatbot with Groq")

# sidebar for settings
st.sidebar.header("⚙ Settings")
api_key=st.sidebar.text_input("Enter Your Groq API KEY:",type="password")

# dropdown to select various groq models
llm=st.sidebar.selectbox("Select an groq model",["llama-3.1-8b-instant","llama-3.3-70b-versatile","openai/gpt-oss-20b"])

# adjust response parameter
temperature=st.sidebar.slider("Temperature",min_value=0.0, max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider("Max Tokens",min_value=50,max_value=1000,value=150)

# main inference for user input
st.write("Go ahead and ask any question")
user_input=st.text_input("You:")

if user_input:
    response=generate_response(user_input,api_key,llm,temperature,max_tokens)
    st.write("💬 Response:")
    st.write(response)
else: 
    st.write("Please provide the query")

