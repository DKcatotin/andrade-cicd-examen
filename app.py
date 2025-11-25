from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({"message": "API Andrade funcionando"}), 200

@app.post("/sumar")
def sumar():
    data = request.get_json()
    a = data.get("a", 0)
    b = data.get("b", 0)
    return jsonify({"resultado": a + b})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
