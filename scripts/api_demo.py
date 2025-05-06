from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any
from esg_lex_harmonizer.input_preprocessing.preprocessor import LegalPreprocessor
from esg_lex_harmonizer.conflict.detector import ConflictDetector
from esg_lex_harmonizer.impact.analyzer import ESGImpactAnalyzer

app = FastAPI(title="ESG-Lex-Harmonizer API Demo")

class LawTextRequest(BaseModel):
    text: str
    external_data: Dict[str, Any] = {}

class ConflictResponse(BaseModel):
    conflicts: List[Dict[str, Any]]

class ESGImpactResponse(BaseModel):
    impact: Dict[str, Any]

preprocessor = LegalPreprocessor()
detector = ConflictDetector()
analyzer = ESGImpactAnalyzer()

@app.post("/preprocess")
def preprocess_law_text(req: LawTextRequest) -> Dict[str, Any]:
    """法規文本預處理（分詞、NER、RE）。"""
    return preprocessor.preprocess_law_text(req.text)

@app.post("/detect_conflict", response_model=ConflictResponse)
def detect_conflict(req: LawTextRequest) -> ConflictResponse:
    """偵測法規內部衝突。"""
    law_data = preprocessor.preprocess_law_text(req.text)
    # 假設 law_data 已結構化
    conflicts = detector.detect_conflicts(law_data)
    return ConflictResponse(conflicts=conflicts)

@app.post("/esg_impact", response_model=ESGImpactResponse)
def esg_impact(req: LawTextRequest) -> ESGImpactResponse:
    """分析衝突對 ESG 的影響。"""
    law_data = preprocessor.preprocess_law_text(req.text)
    conflicts = detector.detect_conflicts(law_data)
    impact = analyzer.analyze_impact(conflicts, req.external_data)
    return ESGImpactResponse(impact=impact)

# 啟動方式： poetry run uvicorn scripts.api_demo:app --reload 