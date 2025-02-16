import requests
import os
from dotenv import load_dotenv, dotenv_values
from flask import Flask, request

load_dotenv()

#print(os.getenv("TOKEN"))

app = Flask(__name__)
BOT_TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def send_telegram_message(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": msg}
    requests.post(url, json=payload)


@app.route('/', methods=['GET'])
def home():
    return {"version":"0.1"}

@app.route('/gitlab-webhook', methods=['POST'])
def gitlab_webhook():
    data = request.json
    event_type = request.headers.get("X-Gitlab-Event")

    mr_title = data["object_attributes"]["title"]
    mr_author = data["user"]["name"]
    link = data["object_attributes"]["url"]
    message = f"🔔 New action, send by {event_type} \n👤 Autor: {mr_author} \n📌 Tytuł: {mr_title} \n🔗 Url: {link}"
    send_telegram_message(message)

    return {"status": "ok"}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=15666, debug=True)
