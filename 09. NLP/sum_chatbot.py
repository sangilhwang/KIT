# pip install Pypdf2==3.0.1
# streamlit run sum_chatbot.py

import os
from PyPDF2 import PdfReader
import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback

os.environ["OPENAI_API_KEY"] = ""

def process_text(text):
    # 텍스트를 청크로 분할
    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )

    chunks = text_splitter.split_text(text)

    # 임베딩 처리(벡터 변환)
    embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")
    documents = FAISS.from_texts(chunks, embeddings)
    return documents

def main():
    st.title("PDF 요약서비스")
    st.divider()
    try:
        os.environ["OPENAI_API_KEY"] = ""
    except ValueError as e:
        st.error(str(e))

    pdf = st.file_uploader("PDF파일을 업로드해주세요", type = "pdf")

    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = "" # text 변수에 PDF 내용을 저장
        for page in pdf_reader.pages:
            text += page.extract_text()

        documents = process_text(text)

        query = "업로드된 PDF 파일의 내용을 3 ~ 5 문장으로 요약해주세요."
        # LLM 에 PDF 파일 요약 요청

        if query:
            docs = documents.similarity_search(query)
            llm = ChatOpenAI(model = "gpt-3.5-turbo", temperature = 0.1)
            chain = load_qa_chain(llm, chain_type = "stuff")

            with get_openai_callback() as cost:
                response = chain.run(input_documents = docs, question = query)
                print(cost)

            st.subheader("--요약 결과--:")
            st.write(response)

if __name__ == "__main__":
    main()
