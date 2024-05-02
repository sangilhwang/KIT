# cmd 터미널 명령어
# conda create -n chatbot_env python==3.8
# conda activate chatbot_env
# pip install langchain
# pip install streamlit==1.29.0
# pip install openai==0.28.1
# pip install pydantic==1.10.9
# streamlit run chatbot.py

import streamlit as st
from langchain.llms import OpenAI
import os
os.environ["OPENAI_API_KEY"] = ""

st.set_page_config(page_title = "뭐든지 질문하세요")
st.title("뭐든지 질문하세요~")

def generate_response(input_text):
    '''
    llm이 답변을 생성하도록 하는 함수
    '''
    llm = OpenAI(model_name = "gpt-3.5-turbo-instruct", temperature = 0.0)
    st.info(llm(input_text))

with st.form("Question"):
    text = st.text_area("질문 입력:", "OpenAI는 어떤 유형의 텍스트 모델을 제공하나요?")
    submitted = st.form_submit_button("보내기")
    generate_response(text)
