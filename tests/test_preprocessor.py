from esg_lex_harmonizer.input_preprocessing.preprocessor import LegalPreprocessor

def test_preprocess_law_text():
    preprocessor = LegalPreprocessor()
    result = preprocessor.preprocess_law_text("第1條：本法規定水資源管理原則。")
    assert isinstance(result, dict)


def test_integrate_external_data():
    preprocessor = LegalPreprocessor()
    law_data = {"條文": "第1條"}
    external_data = {"水文": "數據"}
    result = preprocessor.integrate_external_data(law_data, external_data)
    assert isinstance(result, dict) 