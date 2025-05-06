"""
知識擴充 demo：條文結構化、ESG指標對應、外部資料整合
"""
from typing import List, Dict
import json

def structure_law_articles(articles: List[str]) -> List[Dict[str, str]]:
    """
    將條文簡單結構化（MVP 範例）。
    """
    return [{"條文": art, "主體": "工業用水" if "工業" in art else "其他", "限制": "30%" if "30%" in art else ""} for art in articles]

def map_esg_indicators(articles: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    條文對應 ESG 指標（MVP 範例）。
    """
    for art in articles:
        if "污染" in art["條文"]:
            art["ESG"] = "E"
        elif "分配" in art["條文"]:
            art["ESG"] = "S"
        else:
            art["ESG"] = "G"
    return articles

if __name__ == "__main__":
    articles = ["工業用水不得超過30%", "特殊情況下可達50%", "水污染應依環保法規處理"]
    structured = structure_law_articles(articles)
    mapped = map_esg_indicators(structured)
    print(json.dumps(mapped, ensure_ascii=False, indent=2)) 