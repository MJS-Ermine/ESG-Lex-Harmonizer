from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any, Dict
import json
from pathlib import Path
from esg_lex_harmonizer.conflict.detector import detect_conflicts
from esg_lex_harmonizer.impact.analyzer import evaluate_esg_impact
from esg_lex_harmonizer.harmonizer.recommender import generate_harmonization_suggestion

app = FastAPI(title="ESG-Lex-Harmonizer API")

DATA_PATH = Path(__file__).parent.parent / "data" / "water_law_mock.json"

def load_law_data() -> Dict[str, Any]:
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

class AnalyzeRequest(BaseModel):
    law_text: str | None = None

@app.post("/analyze")
def analyze_law(req: AnalyzeRequest) -> Dict[str, Any]:
    """
    法規衝突偵測 API
    """
    law_data = load_law_data()
    articles = law_data["articles"]
    conflicts = detect_conflicts(articles)
    return {"conflicts": conflicts}

@app.get("/evaluate")
def evaluate_esg() -> Dict[str, Any]:
    """
    ESG 影響評分 API
    """
    law_data = load_law_data()
    esg_scores = evaluate_esg_impact(law_data)
    return {"esg_scores": esg_scores}

@app.get("/suggest")
def suggest_harmonization() -> Dict[str, Any]:
    """
    協調建議生成 API
    """
    law_data = load_law_data()
    suggestion = generate_harmonization_suggestion(law_data)
    return {"suggestion": suggestion} 