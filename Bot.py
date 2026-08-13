import os
import requests

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

def send_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(
        url,
        json={
            "chat_id": CHAT_ID,
            "text": message
        },
        timeout=20
    )

def main():
    message = (
        "🚀 MemeCoin Tracker is working!\n\n"
        "GitHub Actions successfully ran the bot."
    )

    send_message(message)

if __name__ == "__main__":
    main()
