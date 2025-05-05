from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
from transformers import pipeline
import os

PAPER_DIR = os.path.join(os.path.dirname(__file__), '../docs/papers')

# 1. 載入所有 PDF
pdf_files = [os.path.join(PAPER_DIR, f) for f in os.listdir(PAPER_DIR) if f.endswith('.pdf')]
documents = []
for pdf in pdf_files:
    loader = PyPDFLoader(pdf)
    documents.extend(loader.load())

# 2. 切分文本
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_documents(documents)

# 3. 建立向量資料庫
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
vectorstore = FAISS.from_documents(docs, embeddings)

# 4. 建立 LLM pipeline
hf_pipe = pipeline("text2text-generation", model="google/flan-t5-base")
llm = HuggingFacePipeline(pipeline=hf_pipe)

# 5. 建立 RAG QA chain
qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())

if __name__ == "__main__":
    print("RAG pipeline 啟動，請輸入查詢：")
    while True:
        query = input("Q: ")
        if not query:
            break
        result = qa.run(query)
        print(f"A: {result}") 