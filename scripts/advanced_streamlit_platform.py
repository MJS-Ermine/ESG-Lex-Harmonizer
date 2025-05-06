"""
進階 ESG-Lex-Harmonizer 互動平台（類 En-ROADS）
"""
import streamlit as st
import plotly.graph_objects as go
from typing import List, Dict
import requests
import os

st.set_page_config(page_title="ESG-Lex-Harmonizer 進階平台", layout="wide", page_icon="🌏")

# Logo 與標題
st.markdown("""
<div style='display: flex; align-items: center;'>
  <img src='https://raw.githubusercontent.com/MJS-Ermine/ESG-Lex-Harmonizer/main/docs/logo.png' width='60' style='margin-right: 20px;'>
  <h1 style='color: #2E86AB;'>ESG-Lex-Harmonizer 進階互動平台 (En-ROADS 類型)</h1>
</div>
""", unsafe_allow_html=True)

# 分頁
tab1, tab2, tab3 = st.tabs(["決策模擬", "RAG 問答", "知識擴充"])

with tab1:
    st.subheader("決策參數設定")
    laws = ["水利法", "空污法", "能源法"]
    scenarios = ["現行政策", "永續強化", "產業優先"]
    col1, col2 = st.columns(2)
    with col1:
        law = st.selectbox("選擇法規", laws)
    with col2:
        scenario = st.selectbox("選擇情境", scenarios)
    st.markdown("---")
    # 參數滑桿
    water_limit = st.slider("工業用水上限(%)", 10, 80, 30, step=5)
    esg_weight_e = st.slider("E 指標權重", 0, 100, 33)
    esg_weight_s = st.slider("S 指標權重", 0, 100, 33)
    esg_weight_g = st.slider("G 指標權重", 0, 100, 34)
    # ESG 指標雷達圖
    esg_scores = {"E": water_limit/100, "S": esg_weight_s/100, "G": esg_weight_g/100}
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=list(esg_scores.values()), theta=list(esg_scores.keys()), fill='toself', name='ESG', line_color="#2E86AB"))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0,1], showticklabels=True, gridcolor="#BFD7ED")), showlegend=False, title="ESG 指標雷達圖", paper_bgcolor="#F6F9FB")
    st.plotly_chart(fig, use_container_width=True)
    # 報告產生
    if st.button("產生決策建議報告", key="gen_report"):
        st.success(f"建議：{law} 在 {scenario} 下，工業用水上限建議為 {water_limit}%，ESG 權重 E:{esg_weight_e} S:{esg_weight_s} G:{esg_weight_g}")

with tab2:
    st.subheader("法規/ESG 問答 (RAG)")
    API_URL = st.text_input("API URL", os.environ.get("ESG_API_URL", "http://localhost:8000"), key="api_url")
    API_KEY = st.text_input("API Key", os.environ.get("ESG_API_KEY", "demo-key"), type="password", key="api_key")
    rag_query = st.text_input("請輸入法規/ESG 問題：", key="rag_query")
    if st.button("查詢 RAG 答案", key="rag_btn") and rag_query:
        try:
            resp = requests.post(f"{API_URL}/rag_qa", json={"query": rag_query}, headers={"x-api-key": API_KEY}, timeout=10)
            if resp.status_code == 200:
                st.success(f"RAG 回答：{resp.json()['answer']}")
            else:
                st.error(f"API 錯誤：{resp.text}")
        except Exception as e:
            st.error(f"連線失敗：{e}")

with tab3:
    st.subheader("條文知識擴充")
    API_URL = st.text_input("API URL", os.environ.get("ESG_API_URL", "http://localhost:8000"), key="api_url2")
    API_KEY = st.text_input("API Key", os.environ.get("ESG_API_KEY", "demo-key"), type="password", key="api_key2")
    article_input = st.text_area("請輸入條文（每行一條）", key="article_input")
    if st.button("執行知識擴充", key="expand_btn") and article_input:
        articles = [a.strip() for a in article_input.splitlines() if a.strip()]
        try:
            resp = requests.post(f"{API_URL}/expand_knowledge", json={"articles": articles}, headers={"x-api-key": API_KEY}, timeout=10)
            if resp.status_code == 200:
                st.json(resp.json())
            else:
                st.error(f"API 錯誤：{resp.text}")
        except Exception as e:
            st.error(f"連線失敗：{e}")

st.markdown("""
<style>
    .stTabs [data-baseweb="tab"] { font-size:18px; font-weight:600; color:#2E86AB; }
    .stButton>button { background:#2E86AB; color:white; font-weight:600; }
    .stTextInput>div>input { background:#F6F9FB; }
</style>
""", unsafe_allow_html=True) 