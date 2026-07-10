import os
import telebot
import time
import sys

# ۱. دریافت تنظیمات از محیط Railway
BOT_TOKEN = os.getenv('BOT_TOKEN')
raw_channel_id = os.getenv('CHANNEL_ID')
CHANNEL_ID = -100123456789  # <--- دقت کنید: بدون علامت ' ' یا " "

# دریافت از محیط Railway و تبدیل اجباری به عدد صحیح (int)
BOT_TOKEN = os.getenv('BOT_TOKEN')
raw_channel_id = os.getenv('CHANNEL_ID')

if not BOT_TOKEN or not raw_channel_id:
    print("❌ Error: BOT_TOKEN or CHANNEL_ID not found in environment variables!")
    sys.exit(1)

# تبدیل رشته‌ی دریافتی از محیط Railway به عدد صحیح
try:
    CHANNEL_ID = int(raw_channel_id)
except ValueError:
    print(f"❌ Error: CHANNEL_ID '{raw_channel_id}' must be a number (e.g., -100123456789)")
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
