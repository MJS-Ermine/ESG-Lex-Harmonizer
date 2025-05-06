"""
RAG pipeline demo：法規/ESG問答
"""
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

# 假設已經有法規條文向量庫（可用真實資料替換）
docs = ["工業用水不得超過30%", "特殊情況下可達50%", "水污染應依環保法規處理"]
embeddings = HuggingFaceEmbeddings()
vectorstore = FAISS.from_texts(docs, embeddings)
retriever = vectorstore.as_retriever()
llm = OpenAI(temperature=0)
qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

query = "工業用水上限有什麼例外？"
result = qa.run(query)
print("問句：", query)
print("RAG 回答：", result) 