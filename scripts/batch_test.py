import json
from typing import List, Dict, Any
from esg_lex_harmonizer.input_preprocessing.preprocessor import LegalPreprocessor
from esg_lex_harmonizer.conflict.detector import ConflictDetector
from esg_lex_harmonizer.impact.analyzer import ESGImpactAnalyzer
from esg_lex_harmonizer.harmonizer.recommender import HarmonizationRecommender
from esg_lex_harmonizer.evaluation.metrics import EvaluationMetrics

def batch_test(test_cases: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    pre = LegalPreprocessor()
    det = ConflictDetector()
    imp = ESGImpactAnalyzer()
    rec = HarmonizationRecommender()
    evalm = EvaluationMetrics()
    results = []
    for case in test_cases:
        law_text = case["law_text"]
        external_data = case.get("external_data", {})
        reference_conflicts = case.get("reference_conflicts", [])
        reference_recommendations = case.get("reference_recommendations", [])
        law_data = pre.preprocess_law_text(law_text)
        conflicts = det.detect_conflicts(law_data)
        impact = imp.analyze_impact(conflicts, external_data)
        recommendations = rec.generate_recommendations(conflicts, impact)
        conflict_metrics = evalm.evaluate_conflict_detection(conflicts, reference_conflicts)
        rec_metrics = evalm.evaluate_recommendations(recommendations, reference_recommendations)
        results.append({
            "law_text": law_text,
            "conflicts": conflicts,
            "impact": impact,
            "recommendations": recommendations,
            "conflict_metrics": conflict_metrics,
            "rec_metrics": rec_metrics
        })
    return results

if __name__ == "__main__":
    # 範例測試資料
    test_cases = [
        {
            "law_text": "第1條：本法規定水資源管理原則。第2條：水資源不得用於非永續用途。",
            "external_data": {"水文": "嚴重缺水"},
            "reference_conflicts": [],
            "reference_recommendations": []
        }
    ]
    results = batch_test(test_cases)
    print(json.dumps(results, ensure_ascii=False, indent=2)) 