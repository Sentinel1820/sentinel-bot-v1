import os
import time
import requests

# تنظیمات تلگرام (که به صورت متغیرهای محیطی یا مستقیم خوانده می‌شود)
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "YOUR_CHAT_ID")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        print(f"Error sending message: {e}")

def check_market():
    # پیام اولیه تست سیستم
    msg = "🟢 **ایجنت سنتینل روشن شد و در حال رصد ابری بازار است!**"
    send_telegram_message(msg)

if __name__ == "__main__":
    check_market()
    # حلقه ۲۴ ساعته برای اجرای مداوم روی ابر
    while True:
        # در اینجا منطق اصلی رصد بازار و مووینگ‌ها اجرا می‌شود
        time.sleep(3600) # بررسی هر یک ساعت
