import os
from typing import List, Dict
import jieba
from PyPDF2 import PdfReader
from transformers import pipeline

PAPER_DIR = os.path.join(os.path.dirname(__file__), '../docs/papers')


def extract_text_from_pdf(pdf_path: str) -> str:
    """從 PDF 檔案提取全文。"""
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def extract_keywords(text: str, top_k: int = 10) -> List[str]:
    """用 jieba 萃取關鍵詞。"""
    words = jieba.lcut(text)
    freq = {}
    for w in words:
        if len(w) > 1:
            freq[w] = freq.get(w, 0) + 1
    return sorted(freq, key=freq.get, reverse=True)[:top_k]


def summarize_text(text: str, model_name: str = "facebook/bart-large-cnn") -> str:
    """用 transformers summarization pipeline 摘要。"""
    summarizer = pipeline("summarization", model=model_name)
    # 只取前 1024 字元避免超長
    summary = summarizer(text[:1024], max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']


def analyze_papers() -> List[Dict]:
    """批次分析所有 PDF 論文，輸出摘要與關鍵詞。"""
    results = []
    for fname in os.listdir(PAPER_DIR):
        if fname.endswith('.pdf'):
            path = os.path.join(PAPER_DIR, fname)
            text = extract_text_from_pdf(path)
            keywords = extract_keywords(text)
            try:
                summary = summarize_text(text)
            except Exception:
                summary = "(摘要失敗)"
            results.append({
                "file": fname,
                "keywords": keywords,
                "summary": summary
            })
    return results


if __name__ == "__main__":
    papers = analyze_papers()
    for paper in papers:
        print(f"檔案: {paper['file']}")
        print(f"關鍵詞: {paper['keywords']}")
        print(f"摘要: {paper['summary']}")
        print("-" * 40) 