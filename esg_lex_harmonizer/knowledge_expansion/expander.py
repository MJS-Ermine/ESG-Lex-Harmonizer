from typing import List, Dict
from transformers import pipeline

class ArticleExpander:
    def __init__(self):
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        # 假設關鍵字分類
        self.keywords = {"E": ["水", "污染", "能源"], "S": ["社會", "勞工"], "G": ["治理", "法規"]}

    def classify(self, article: str) -> str:
        for k, kws in self.keywords.items():
            if any(kw in article for kw in kws):
                return k
        return "G"

    def expand(self, articles: List[str]) -> List[Dict[str, str]]:
        results = []
        for art in articles:
            summary = self.summarizer(art, max_length=30, min_length=5, do_sample=False)[0]["summary_text"]
            esg = self.classify(art)
            results.append({"條文": art, "ESG": esg, "摘要": summary})
        return results 