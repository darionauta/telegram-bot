import os
from dotenv import load_dotenv, dotenv_values
from flask import Flask, request

load_dotenv()

#print(os.getenv("TOKEN"))

app = Flask(__name__)
BOT_TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def send_telegram_message(msg)
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": msg}


@app.route('/gitlab-webhook', methods=['POST'])
def gitlab_webhook():
    data = request.json
    event_type = request.headers.get("X-Gitlab-Event")

    if event_type == "Merge Request Hook":
        mr_title = data["object_attributes"]["title"]
        mr_author = data["user"]["name"]
        message = f"🔔 Nowy Merge Request! \n👤 Autor: {mr_author} \n📌 Tytuł: {mr_title}"
        send_telegram_message(message)

    elif event_type == "Issue Hook":
        issue_title = data["object_attributes"]["title"]
        issue_author = data["user"]["name"]
        message = f"⚠️ Nowy Issue! \n👤 Autor: {issue_author} \n📌 Tytuł: {issue_title}"
        send_telegram_message(message)

    return {"status": "ok"}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=15666, debug=True)
