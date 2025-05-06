from typing import List, Dict, Any

class HarmonizationRecommender:
    """協調/修法建議生成器。

    根據衝突分析與 ESG 影響評估，自動生成法規協調建議。
    """
    def __init__(self) -> None:
        """初始化建議生成器。"""
        pass

    def generate_recommendations(self, conflicts: List[Dict[str, Any]], esg_impact: Dict[str, Any]) -> List[str]:
        """根據衝突與 ESG 影響，生成協調/修法建議。

        Args:
            conflicts (List[Dict[str, Any]]): 偵測到的法律衝突。
            esg_impact (Dict[str, Any]): ESG 影響分析結果。

        Returns:
            List[str]: 法規協調或修法建議清單。
        """
        recommendations = []
        for conflict in conflicts:
            if conflict["type"] == "邏輯矛盾":
                recommendations.append("建議修正條文以消除邏輯矛盾")
            if conflict["type"] == "定義不一致":
                recommendations.append(f"建議統一『{conflict['term']}』定義")
        # 根據 ESG 影響調整建議
        if esg_impact.get("E", 0) > 1:
            recommendations.append("建議優先考慮環境永續性修法")
        # TODO: 可結合 LLM 生成更細緻建議
        return recommendations

def generate_harmonization_suggestion(law_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    根據 law_data 回傳協調建議（MVP 版）。

    Args:
        law_data (Dict[str, Any]): 法規資料

    Returns:
        Dict[str, Any]: 協調建議
    """
    conflicts = law_data.get("conflicts", [])
    suggestions = []
    for c in conflicts:
        if c["type"] == "比例上限衝突":
            suggestions.append("建議統一工業用水上限比例，避免執行混亂。")
    if not suggestions:
        suggestions.append("未發現重大衝突，建議定期檢討法規。")
    return {"suggestions": suggestions} 