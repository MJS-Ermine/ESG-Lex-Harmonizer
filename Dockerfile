# syntax=docker/dockerfile:1
FROM python:3.10-slim

# 安裝系統依賴
RUN apt-get update && apt-get install -y build-essential git && rm -rf /var/lib/apt/lists/*

# 設定工作目錄
WORKDIR /app

# 複製 Poetry 設定檔
COPY pyproject.toml poetry.lock ./

# 安裝 Poetry
RUN pip install poetry && poetry config virtualenvs.create false

# 安裝 Python 依賴
RUN poetry install --no-interaction --no-ansi

# 複製專案檔案
COPY . .

# 預設啟動 FastAPI 與 Streamlit
CMD ["bash", "-c", "uvicorn esg_lex_harmonizer.api.advanced_api:app --host 0.0.0.0 --port 8000 & streamlit run scripts/advanced_streamlit_platform.py --server.port 8501"] 