from esg_lex_harmonizer.impact.analyzer import ESGImpactAnalyzer

def test_analyze_impact():
    analyzer = ESGImpactAnalyzer()
    conflicts = [{"type": "邏輯矛盾", "條文": "第1條"}]
    external_data = {"水文": "數據"}
    result = analyzer.analyze_impact(conflicts, external_data)
    assert isinstance(result, dict)
    assert "E" in result and "S" in result and "G" in result 