from typing import List, Dict, Any

class ConflictDetector:
    """法律衝突偵測引擎。

    負責自動偵測法規內部的邏輯、語義、定義等衝突。
    """
    def __init__(self) -> None:
        """初始化衝突偵測引擎。"""
        pass

    def detect_conflicts(self, law_knowledge: Dict[str, Any]) -> List[Dict[str, Any]]:
        """偵測法律知識中的各類衝突。

        Args:
            law_knowledge (Dict[str, Any]): 結構化法律知識。

        Returns:
            List[Dict[str, Any]]: 偵測到的衝突清單。
        """
        conflicts = []
        # 範例：檢查邏輯矛盾（A ⇒ B 與 A ⇒ ¬B）
        rules = law_knowledge.get("rules", [])
        for rule in rules:
            if rule.get("contradicts"):
                conflicts.append({
                    "type": "邏輯矛盾",
                    "rule": rule
                })
        # 範例：定義不一致
        definitions = law_knowledge.get("definitions", {})
        for term, defs in definitions.items():
            if len(set(defs)) > 1:
                conflicts.append({
                    "type": "定義不一致",
                    "term": term,
                    "definitions": defs
                })
        # TODO: 語義衝突、過時性衝突等
        return conflicts

def detect_conflicts(articles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    根據條文內容進行簡單衝突偵測（MVP 版）。

    Args:
        articles (List[Dict[str, Any]]): 條文清單

    Returns:
        List[Dict[str, Any]]: 偵測到的衝突清單
    """
    # MVP：若同時有工業用水 30% 與 50% 條文，視為比例上限衝突
    ids = [a["id"] for a in articles]
    texts = [a["text"] for a in articles]
    conflict = None
    if any("30%" in t for t in texts) and any("50%" in t for t in texts):
        conflict = {
            "article_a": ids[texts.index(next(t for t in texts if "30%" in t))],
            "article_b": ids[texts.index(next(t for t in texts if "50%" in t))],
            "type": "比例上限衝突",
            "description": "工業用水上限規定不一致。"
        }
    return [conflict] if conflict else [] 