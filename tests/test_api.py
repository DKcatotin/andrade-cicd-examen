import requests
import json
from multiprocessing import Process
import time
import app as app_module

# We'll run the Flask app in a subprocess for the tests
def run_app():
    app_module.app.run(host="0.0.0.0", port=8081)

def test_analyze_endpoint():
    # start app
    p = Process(target=run_app, daemon=True)
    p.start()
    time.sleep(1.0)  # short wait for server to start

    try:
        url = "http://127.0.0.1:8081/analyze"
        payload = {"text": "Me encanta la pizza y la focaccia, comida italiana."}
        r = requests.post(url, json=payload, timeout=5)
        assert r.status_code == 200
        body = r.json()
        assert "category" in body
        assert body["category"] in ["food", "tech", "health", "other"]
    finally:
        p.terminate()
        p.join(timeout=1)
