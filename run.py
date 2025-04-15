import requests

text = "This project is going terribly wrong."

response = requests.post(
    "http://127.0.0.1:5000/analyze",
    json={"text": text}
)

print("Response:", response.json())

