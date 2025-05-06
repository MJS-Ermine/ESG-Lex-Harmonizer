# ESG-Lex-Harmonizer

ESG-Lex-Harmonizer 是一個計算法學原型系統，專為自動偵測、分析 ESG 相關法律法規（以水資源管理法規為核心案例）內部矛盾與不一致性而設計。系統能整合外部科學、經濟、社會等多維度數據，從永續性（環境 E、社會 S、治理 G）角度評估法律衝突的實際影響，並生成數據驅動的法規協調或修訂建議。

## 專案目標
- 自動化偵測法規內部邏輯、語義、定義等衝突
- 整合外部 ESG 多源數據，量化衝突影響
- 生成技術性法規協調建議，促進 ESG 目標
- 支援法學、NLP、知識圖譜、RAG 等多種技術

## 主要模組
- `esg_lex_harmonizer/`：主程式與核心模組
- `docs/`：論文、法規、技術文件
- `tests/`：pytest 單元測試
- `esg_lex_harmonizer/input_preprocessing/`：法規文本解析、外部數據整合
- `esg_lex_harmonizer/conflict/`：法律衝突偵測引擎
- `esg_lex_harmonizer/impact/`：ESG 影響分析
- `esg_lex_harmonizer/harmonizer/`：協調建議生成
- `esg_lex_harmonizer/evaluation/`：評估與可視化

## 安裝方式
```bash
# 建議使用 Poetry
poetry install
```

## 開發者指引
- Python 3.10+
- 依賴管理：Poetry
- 格式化/靜態檢查：ruff
- 測試：pytest
- 主要依賴：transformers, spacy, jieba, pandas, torch, langchain, llama-index, streamlit

## 參考文獻與資源
- 21 篇法學/NLP 論文（見 docs/papers/）
- 相關 GitHub 倉庫資源（BLADE, DELTA, LexEval...）

## 聯絡方式
- Maintainer: MJS-Ermine