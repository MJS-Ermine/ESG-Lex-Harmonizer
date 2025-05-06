import streamlit as st
from esg_lex_harmonizer.input_preprocessing.preprocessor import LegalPreprocessor
from esg_lex_harmonizer.conflict.detector import ConflictDetector
from esg_lex_harmonizer.impact.analyzer import ESGImpactAnalyzer

st.set_page_config(page_title="ESG-Lex-Harmonizer Demo", layout="wide")
st.title("ESG-Lex-Harmonizer 法規衝突與ESG分析互動Demo")

preprocessor = LegalPreprocessor()
detector = ConflictDetector()
analyzer = ESGImpactAnalyzer()

law_text = st.text_area("請輸入法規條文（可貼多條）", height=200)
external_data = st.text_input("外部 ESG 數據（如：水文=嚴重缺水）", "水文=嚴重缺水")

if st.button("分析！"):
    st.subheader("分詞/NER 結果")
    law_data = preprocessor.preprocess_law_text(law_text)
    st.json(law_data)

    st.subheader("衝突偵測結果")
    conflicts = detector.detect_conflicts(law_data)
    st.json(conflicts)

    st.subheader("ESG 影響分析")
    # 將外部數據轉為 dict
    ext_dict = dict([kv.split("=") for kv in external_data.split(",") if "=" in kv])
    impact = analyzer.analyze_impact(conflicts, ext_dict)
    st.json(impact)

st.info("本Demo僅供原型展示，所有分析結果僅供參考。") 