import os
import telebot
import time
import sys

# ۱. دریافت تنظیمات از محیط Railway
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_ID = '@forward_test'

# بررسی وجود توکن
if not BOT_TOKEN:
    print("❌ Error: BOT_TOKEN not found in environment variables!")
    sys.exit(1)

bot = telebot.TeleBot(BOT_TOKEN)

# ۲. هندلر فوروارد کردن پیام‌ها
@bot.message_handler(func=lambda message: True)
def forward_to_channel(message):
    try:
        # فوروارد پیام به کانال
        bot.forward_message(CHANNEL_ID, message.chat.id, message.message_id)
        print(f"📨 Message forwarded from {message.chat.id}")
    except Exception as e:
        print(f"⚠️ Error during forwarding: {e}")

# ۳. اجرای اصلی ربات با ساختار ضد خاموش شدن
def run_bot():
    print("🚀 Bot is starting up and polling...")
    while True:
        try:
            # استفاده از infinity_polling با تنظیمات پایدار
            bot.infinity_polling(timeout=60, long_polling_timeout=60)
        except Exception as e:
            print(f"⚠️ Connection error: {e}")
            print("⏳ Restarting in 10 seconds...")
            time.sleep(10) # مکث کوتاه برای جلوگیری از فشار به سرور در صورت قطعی

if __name__ == "__main__":
    print("✅ Bot script initialized successfully.")
    run_bot()
