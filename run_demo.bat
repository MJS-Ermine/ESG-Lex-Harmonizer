@echo off
REM === 一鍵啟動 ESG-Lex-Harmonizer 進階平台 ===
REM 啟動 FastAPI API（後端）
start cmd /k "cd /d %~dp0 && cd ESG-Lex-Harmonizer && ..\venv310\Scripts\activate.bat && uvicorn esg_lex_harmonizer.api.advanced_api:app --reload"
REM 啟動 Streamlit 前端
start cmd /k "cd /d %~dp0 && venv310\Scripts\activate.bat && streamlit run ESG-Lex-Harmonizer\scripts\advanced_streamlit_platform.py"
REM 等待前端啟動後自動打開瀏覽器
ping 127.0.0.1 -n 5 > nul
start http://localhost:8501
REM 顯示提示
@echo.
@echo === ESG-Lex-Harmonizer 進階平台已啟動 ===
@echo API Key: demo-key
@echo 如需關閉，請手動關閉兩個新開的命令視窗。
@echo ========================================= 