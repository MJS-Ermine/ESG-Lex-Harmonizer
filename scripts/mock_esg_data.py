import random
import json
from typing import Dict, Any

def generate_mock_esg_data() -> Dict[str, Any]:
    """產生一筆隨機 ESG 外部數據。"""
    return {
        "水文": random.choice(["正常", "偏枯", "嚴重缺水"]),
        "氣象": random.choice(["晴", "雨", "旱", "颱風"]),
        "碳排放": round(random.uniform(0.5, 2.5), 2),
        "社會調查": random.choice(["滿意", "普通", "不滿意"]),
        "生物多樣性": random.choice(["高", "中", "低"]),
        "經濟影響": random.choice(["正面", "中性", "負面"])
    }

def batch_generate(n: int = 10):
    """批次產生 n 筆 ESG 外部數據。"""
    return [generate_mock_esg_data() for _ in range(n)]

if __name__ == "__main__":
    data = batch_generate(20)
    print(json.dumps(data, ensure_ascii=False, indent=2)) 