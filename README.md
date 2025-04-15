# 🧠 Sentiment Analysis API (Flask + Hugging Face)

This project deploys a **pre-trained sentiment analysis model** from Hugging Face (`distilbert-base-uncased-finetuned-sst-2-english`) as a **RESTful API** using **Flask**. You can send text to the API and receive a **positive or negative** sentiment prediction.

---

## 📁 Project Structure

```
sentiment_api/
│
├── app.py               # Flask API exposing the model
├── run.py               # Test script to call the API
├── requirements.txt     # Python dependencies
└── .env                 # Hugging Face API key (not committed to Git)
```

---

## 🚀 Features

- Uses Hugging Face's inference API (no training required)
- Lightweight deployment via Flask
- Simple endpoint to analyze text sentiment
- Organized for easy GitHub collaboration

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/sentiment-api.git
cd sentiment-api
```

### 2. Create & Activate a Virtual Environment (Optional but Recommended)

```bash
python -m venv ai_api_env
source ai_api_env/bin/activate   # macOS/Linux
ai_api_env\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your Hugging Face API Token

Create a `.env` file in the root directory:

```env
HF_API_TOKEN=your_huggingface_api_token_here
```

You can get a token from: https://huggingface.co/settings/tokens

---

## ▶️ Run the API Server

```bash
python app.py
```

The server will run at:  
📍 `http://127.0.0.1:5000`

---

## 📬 Using the API

### 🔁 POST Request to `/analyze`

Send a JSON body with a `"text"` field to get the sentiment:

```bash
curl -X POST http://127.0.0.1:5000/analyze \
     -H "Content-Type: application/json" \
     -d '{"text": "I love this app!"}'
```

### 🧪 Or run `run.py`

```bash
python run.py
```

### ✅ Sample Response

```json
[
  {
    "label": "POSITIVE",
    "score": 0.9991232752799988
  }
]
```

---

## 🤝 GitHub Collaboration Guidelines

- Use **feature branches** for changes (e.g., `feature/frontend-form`)
- Make frequent commits with descriptive messages
- Create **Pull Requests** to merge into `main`
- Review and comment on teammate’s code before merging

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [Hugging Face Transformers](https://huggingface.co/models)
- [Flask Web Framework](https://flask.palletsprojects.com/)


