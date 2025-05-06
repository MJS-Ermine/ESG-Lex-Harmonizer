from esg_lex_harmonizer.conflict.detector import ConflictDetector
 
def test_detect_conflicts():
    detector = ConflictDetector()
    law_knowledge = {"條文": "第1條"}
    result = detector.detect_conflicts(law_knowledge)
    assert isinstance(result, list) 