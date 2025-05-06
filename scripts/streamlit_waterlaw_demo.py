"""
Streamlit demo：水利法 ESG 衝突分析互動平台
"""
import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go

API_URL = "http://localhost:8000"

st.title("水利法 ESG 衝突分析互動平台 (MVP)")

# 衝突偵測
if st.button("執行衝突偵測"):
    resp = requests.post(f"{API_URL}/analyze", json={})
    conflicts = resp.json().get("conflicts", [])
    st.subheader("偵測到的衝突")
    st.write(conflicts)

# ESG 評分
if st.button("取得 ESG 影響評分"):
    resp = requests.get(f"{API_URL}/evaluate")
    esg = resp.json().get("esg_scores", {})
    st.subheader("ESG 指標分數")
    st.write(esg)
    if esg:
        fig = go.Figure()
        fig.add_trace(go.Bar(x=list(esg.keys()), y=[v for v in esg.values()]))
        fig.update_layout(title="ESG 指標分布", yaxis_title="分數")
        st.plotly_chart(fig)

# 協調建議
if st.button("取得協調建議"):
    resp = requests.get(f"{API_URL}/suggest")
    suggestion = resp.json().get("suggestion", {})
    st.subheader("協調/修法建議")
    st.write(suggestion) 