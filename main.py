import os
import requests

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = "@material_daily_price"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=data)

send_message("سیستم پایش قیمت آهن فعال شد")
