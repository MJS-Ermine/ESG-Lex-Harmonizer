"""
進階 ESG-Lex-Harmonizer API，安全包裝 RAG pipeline 與知識擴充功能。
"""
from fastapi import FastAPI, HTTPException, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict
import os
from esg_lex_harmonizer.rag.pipeline import SimpleRAG
from esg_lex_harmonizer.knowledge_expansion.expander import ArticleExpander

# === 安全設計：API Key 驗證 ===
API_KEY = os.environ.get("ESG_API_KEY", "demo-key")

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

app = FastAPI(title="ESG-Lex-Harmonizer Advanced API")

# CORS 設定：僅允許本地前端
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === RAG 問答 API ===
class RagQuery(BaseModel):
    query: str

rag_pipeline = SimpleRAG()

@app.post("/rag_qa", dependencies=[Depends(verify_api_key)])
def rag_qa(req: RagQuery) -> Dict[str, str]:
    result = rag_pipeline.query(req.query)
    return {"query": req.query, "answer": result["answer"], "source": result["source"]}

# === 知識擴充 API ===
class KnowledgeRequest(BaseModel):
    articles: List[str]

expander = ArticleExpander()

@app.post("/expand_knowledge", dependencies=[Depends(verify_api_key)])
def expand_knowledge(req: KnowledgeRequest) -> List[Dict[str, str]]:
    return expander.expand(req.articles) 