from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
API_TOKEN = os.getenv("HF_API_TOKEN")
HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}

app = Flask(__name__)

def query_huggingface(text):
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' in request"}), 400

    result = query_huggingface(data["text"])
    return jsonify(result)

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Sentiment Analysis API!"

if __name__ == "__main__":
    app.run(debug=True)


