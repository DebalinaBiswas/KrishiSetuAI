from flask import Flask, request, jsonify
from flask_cors import CORS
from agent import run_agent

app = Flask(__name__)

CORS(app)
@app.route('/')
def home():
    return "KrishiSetu AI Backend Running!"
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    query = data.get("query", "")

    if not query:
        return jsonify({
            "error": "Query is required"
        }), 400

    response = run_agent(query)

    return jsonify({
        "response": response
    })


if __name__ == "__main__":
    app.run(debug=True)