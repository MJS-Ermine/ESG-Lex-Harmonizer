from typing import Dict
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA

# 假設有一組法規條文
DOCUMENTS = [
    {"title": "水利法第1條", "content": "工業用水不得超過30%。"},
    {"title": "水利法第2條", "content": "特殊情況下工業用水可達50%。"},
    {"title": "空污法第1條", "content": "工廠排放需符合標準。"},
]

class SimpleRAG:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.db = FAISS.from_texts([d["content"] for d in DOCUMENTS], self.embeddings)
        self.llm = HuggingFacePipeline.from_model_id(
            model_id="gpt2",
            task="text-generation",
            model_kwargs={"max_length": 128}
        )
        self.qa = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=self.db.as_retriever(),
            chain_type="stuff",
            return_source_documents=True
        )

    def query(self, question: str) -> Dict[str, str]:
        result = self.qa({"query": question})
        answer = result["result"]
        source = result["source_documents"][0].page_content if result["source_documents"] else ""
        return {"answer": answer, "source": source} 