from typing import List, Dict, Any

class EvaluationMetrics:
    """評估指標模組。

    用於評估衝突偵測與建議方案的準確度、有效性等。
    """
    def __init__(self) -> None:
        """初始化評估指標模組。"""
        pass

    def evaluate_conflict_detection(self, detected: List[Dict[str, Any]], ground_truth: List[Dict[str, Any]]) -> Dict[str, float]:
        """評估衝突偵測的準確度與覆蓋率。

        Args:
            detected (List[Dict[str, Any]]): 偵測到的衝突。
            ground_truth (List[Dict[str, Any]]): 標註的正確衝突。

        Returns:
            Dict[str, float]: 各項評估指標（如 precision, recall, f1）。
        """
        # 簡單以條文為 key 計算
        detected_set = set([str(d.get("條文")) for d in detected])
        truth_set = set([str(g.get("條文")) for g in ground_truth])
        tp = len(detected_set & truth_set)
        fp = len(detected_set - truth_set)
        fn = len(truth_set - detected_set)
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
        return {"precision": precision, "recall": recall, "f1": f1}

    def evaluate_recommendations(self, recommendations: List[str], reference: List[str]) -> Dict[str, float]:
        """評估協調建議的有效性。

        Args:
            recommendations (List[str]): 生成的建議。
            reference (List[str]): 參考標準建議。

        Returns:
            Dict[str, float]: 各項評估指標。
        """
        rec_set = set(recommendations)
        ref_set = set(reference)
        tp = len(rec_set & ref_set)
        fp = len(rec_set - ref_set)
        fn = len(ref_set - rec_set)
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
        return {"precision": precision, "recall": recall, "f1": f1} 