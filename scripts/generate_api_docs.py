import requests
import os
from typing import Any

def save_openapi_schema(api_url: str, out_path: str) -> None:
    """下載 FastAPI OpenAPI schema 並儲存為 markdown 文件。

    Args:
        api_url (str): FastAPI API base URL
        out_path (str): 輸出 markdown 路徑
    """
    resp = requests.get(f"{api_url}/openapi.json")
    resp.raise_for_status()
    schema = resp.json()
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"# OpenAPI 文件 ({api_url})\n\n")
        for path, methods in schema.get("paths", {}).items():
            f.write(f"## {path}\n")
            for method, detail in methods.items():
                f.write(f"### {method.upper()}\n")
                f.write(f"**摘要**: {detail.get('summary', '')}\n\n")
                f.write(f"**描述**: {detail.get('description', '')}\n\n")
                f.write(f"**參數**: {detail.get('parameters', [])}\n\n")
                f.write(f"**回應**: {detail.get('responses', {})}\n\n")
                f.write("---\n")

if __name__ == "__main__":
    api_url = os.environ.get("ESG_API_URL", "http://localhost:8000")
    out_path = "../docs/api_docs.md"
    save_openapi_schema(api_url, out_path)
    print(f"API 文件已產生於 {out_path}") 