"""
自動產生水利法 mock data，存為 data/water_law_mock.json。
可擴充支援多法規。
"""
import json
from pathlib import Path

def generate_water_law_mock_data(output_path: str) -> None:
    """
    產生水利法 mock data 並寫入指定路徑。

    Args:
        output_path (str): 輸出檔案路徑
    """
    data = {
        "law_name": "水利法",
        "articles": [
            {"id": 1, "text": "第一條：為管理水資源，特制定本法。"},
            {"id": 2, "text": "第二條：水資源應合理分配，兼顧生態與社會需求。"},
            {"id": 3, "text": "第三條：工業用水不得超過總用水量之 30%。"},
            {"id": 4, "text": "第四條：特殊情況下，工業用水可達 50%。"},
            {"id": 5, "text": "第五條：水污染應依環保法規處理。"}
        ],
        "conflicts": [
            {"article_a": 3, "article_b": 4, "type": "比例上限衝突", "description": "工業用水上限規定不一致。"}
        ],
        "esg_indicators": {
            "E": {"water_saving": 0.8, "pollution_control": 0.7},
            "S": {"public_access": 0.6, "fair_distribution": 0.9},
            "G": {"transparency": 0.7, "compliance": 0.8}
        }
    }
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    generate_water_law_mock_data("../esg_lex_harmonizer/data/water_law_mock.json")
    print("水利法 mock data 已產生！") 