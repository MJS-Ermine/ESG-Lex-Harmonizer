import os
from typing import List
import networkx as nx
import matplotlib.pyplot as plt
import jieba
from PyPDF2 import PdfReader

PAPER_DIR = os.path.join(os.path.dirname(__file__), '../docs/papers')


def extract_text_from_pdf(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def build_knowledge_graph(texts: List[str]) -> nx.Graph:
    """以關鍵詞共現為例建構簡單知識圖譜。"""
    G = nx.Graph()
    for text in texts:
        words = list(set(jieba.lcut(text)))
        for i, w1 in enumerate(words):
            for w2 in words[i+1:]:
                if G.has_edge(w1, w2):
                    G[w1][w2]['weight'] += 1
                else:
                    G.add_edge(w1, w2, weight=1)
    return G


def visualize_graph(G: nx.Graph, out_path: str = "knowledge_graph.png") -> None:
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, k=0.3)
    nx.draw(G, pos, with_labels=True, node_size=50, font_size=8)
    plt.savefig(out_path)
    plt.close()


def main():
    texts = []
    for fname in os.listdir(PAPER_DIR):
        if fname.endswith('.pdf'):
            path = os.path.join(PAPER_DIR, fname)
            texts.append(extract_text_from_pdf(path))
    G = build_knowledge_graph(texts)
    visualize_graph(G)
    print(f"知識圖譜節點數: {G.number_of_nodes()}，邊數: {G.number_of_edges()}")
    print("圖譜已儲存為 knowledge_graph.png")


if __name__ == "__main__":
    main() 