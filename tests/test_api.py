from fastapi.testclient import TestClient
from esg_lex_harmonizer.api.main import app

client = TestClient(app)

def test_analyze():
    resp = client.post("/analyze", json={})
    assert resp.status_code == 200
    assert "conflicts" in resp.json()

def test_evaluate():
    resp = client.get("/evaluate")
    assert resp.status_code == 200
    assert "esg_scores" in resp.json()

def test_suggest():
    resp = client.get("/suggest")
    assert resp.status_code == 200
    assert "suggestion" in resp.json() 