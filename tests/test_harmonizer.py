import pytest
from esg_lex_harmonizer.harmonizer.recommender import HarmonizationRecommender

def test_generate_recommendations():
    recommender = HarmonizationRecommender()
    conflicts = [{"條文": "第1條"}]
    esg_impact = {"E": 0.5, "S": 0.3, "G": 0.2}
    result = recommender.generate_recommendations(conflicts, esg_impact)
    assert isinstance(result, list) 