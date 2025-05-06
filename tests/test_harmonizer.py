from esg_lex_harmonizer.harmonizer.recommender import HarmonizationRecommender

def test_generate_recommendations():
    recommender = HarmonizationRecommender()
    conflicts = [{"type": "邏輯矛盾", "條文": "第1條"}]
    esg_impact = {"E": 0.5, "S": 0.3, "G": 0.2}
    result = recommender.generate_recommendations(conflicts, esg_impact)
    assert isinstance(result, list)
    assert any("邏輯矛盾" in r for r in result) 