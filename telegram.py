import os
from dotenv import load_dotenv
import requests

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message(text: str):
    """Send plain text message to Telegram."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    resp = requests.post(url, data=payload)
    if resp.status_code != 200:
        raise Exception(f"Error sending message: {resp.text}")
    return resp.json()

def send_telegram_file(file_path: str, caption: str = ""):
    """Send file (e.g. PDF, MP3) to Telegram."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    with open(file_path, "rb") as f:
        files = {"document": f}
        data = {"chat_id": CHAT_ID, "caption": caption}
        resp = requests.post(url, data=data, files=files)
    if resp.status_code != 200:
        raise Exception(f"Error sending file: {resp.text}")
    return resp.json()
