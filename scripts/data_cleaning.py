import os
import json
import csv

def clean_text(text: str) -> str:
    """簡單正規化：去除多餘空白、換行。"""
    return ' '.join(text.split())

def clean_txt_dir(txt_dir: str) -> None:
    """批次清理 txt 目錄下所有檔案。"""
    for fname in os.listdir(txt_dir):
        if fname.endswith('.txt'):
            path = os.path.join(txt_dir, fname)
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
            cleaned = clean_text(text)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(cleaned)

def csv_to_json(csv_path: str, json_path: str) -> None:
    """將 CSV 轉為 JSON。"""
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)

def json_to_csv(json_path: str, csv_path: str) -> None:
    """將 JSON 轉為 CSV。"""
    with open(json_path, 'r', encoding='utf-8') as f:
        rows = json.load(f)
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        if rows:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)

def main():
    # 範例：清理 txt 目錄
    # clean_txt_dir('./data/txt')
    # 範例：格式轉換
    # csv_to_json('data.csv', 'data.json')
    # json_to_csv('data.json', 'data.csv')
    pass

if __name__ == "__main__":
    main() 