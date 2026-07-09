import os
import telebot
import time

# خواندن توکن از متغیرهای محیطی Railway
BOT_TOKEN = os.getenv('BOT_TOKEN')

# اگر توکن پیدا نشد، برنامه متوقف شود تا خطا در لاگ‌ها مشخص شود
if not BOT_TOKEN:
    print("❌ Error: BOT_TOKEN not found in environment variables!")
    exit(1)

bot = telebot.TeleBot(BOT_TOKEN)
CHANNEL_ID = '-1004384751215' # آیدی کانال شما

print("🚀 Bot is starting up...")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! ربات با موفقیت در Railway فعال شد. 😊")

# در اینجا کدهای اصلی خودت (مثل فوروارد کردن پیام‌ها) را قرار بده

print("✅ Bot is running and polling...")

# استفاده از infinity_polling برای پایداری بالا در برابر قطع شدن اینترنت
while True:
    try:
        bot.infinity_polling(timeout=60, long_polling_timeout=60)
    except Exception as e:
        print(f"⚠️ Connection error: {e}. Retrying in 5 seconds...")
        time.sleep(5)
