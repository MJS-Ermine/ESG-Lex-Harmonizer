import os
import requests
from typing import List, Dict

GITHUB_USER = "MJS-Ermine"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # 建議放在 .env
KEYWORDS = [
    "BLADE", "CaseGen", "DELTA", "Evaluation Ethics", "EMV", "Investigating Conversational Agent",
    "J&H", "JuDGE", "JUREX-4E", "Knowledge Editing", "LawFlow", "LegalAgentBench", "LeKUBE",
    "LexPam", "LexRAG", "LARGE", "Leveraging Event Schema", "LexEval", "STARD", "Unsupervised Real-Time Hallucination"
]


def fetch_repos(user: str) -> List[Dict]:
    """抓取指定用戶的所有 GitHub repo。"""
    url = f"https://api.github.com/users/{user}/repos?per_page=100"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json()


def match_keywords(repo: Dict, keywords: List[str]) -> List[str]:
    """比對 repo 名稱與描述中的關鍵字。"""
    text = (repo.get("name", "") + " " + repo.get("description", "")).lower()
    return [kw for kw in keywords if kw.lower() in text]


def analyze_github_resources() -> List[Dict]:
    repos = fetch_repos(GITHUB_USER)
    results = []
    for repo in repos:
        matched = match_keywords(repo, KEYWORDS)
        if matched:
            results.append({
                "name": repo["name"],
                "url": repo["html_url"],
                "description": repo.get("description", ""),
                "matched_keywords": matched
            })
    return results


if __name__ == "__main__":
    resources = analyze_github_resources()
    for res in resources:
        print(f"Repo: {res['name']}")
        print(f"URL: {res['url']}")
        print(f"描述: {res['description']}")
        print(f"關聯關鍵字: {res['matched_keywords']}")
        print("-" * 40) 