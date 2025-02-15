import os
from dotenv import load_dotenv, dotenv_values
import requests


load_dotenv()

BOT_TOKEN = os.getenv("TOKEN")

response = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates")
print(response.json())
