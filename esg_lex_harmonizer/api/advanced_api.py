"""
進階 ESG-Lex-Harmonizer API，安全包裝 RAG pipeline 與知識擴充功能。
"""
from fastapi import FastAPI, HTTPException, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict
import os

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

@app.post("/rag_qa", dependencies=[Depends(verify_api_key)])
def rag_qa(req: RagQuery) -> Dict[str, str]:
    # TODO: 真正串接 RAG pipeline，這裡用假資料
    if "例外" in req.query:
        answer = "特殊情況下工業用水可達50%。"
    else:
        answer = "工業用水不得超過30%。"
    return {"query": req.query, "answer": answer}

# === 知識擴充 API ===
class KnowledgeRequest(BaseModel):
    articles: List[str]

@app.post("/expand_knowledge", dependencies=[Depends(verify_api_key)])
def expand_knowledge(req: KnowledgeRequest) -> List[Dict[str, str]]:
    # TODO: 真正串接知識擴充模組，這裡用假資料
    return [{"條文": art, "ESG": "E" if "污染" in art else "G"} for art in req.articles] 