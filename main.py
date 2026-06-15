
import requests

TOKEN = "8957547593:AAGUNoxn0aku5Pv5ukzqUiDr6WTQmXdgf2w"

CHAT_ID = "@material_daily_price"

def send_message(text):

url = f"https://api.telegram.org/bot8957547593:AAGUNoxn0aku5Pv5ukzqUiDr6WTQmXdgf2w/sendMessage"

data = {

"chat_id": CHAT_ID,

"تست اولیه": text
import os

print("TOKEN:", os.environ.get("BOT_TOKEN"))
}
