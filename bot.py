import os
import telebot
import time
import sys

# ۱. دریافت تنظیمات از محیط Railway
BOT_TOKEN = os.getenv('BOT_TOKEN')
# حتماً دقت کنید که آیدی عددی باشد و با -100 شروع شود
# اگر در Railway ست کردید، این خط را تغییر ندهید اما مطمئن شوید در Railway عدد است
CHANNEL_ID = int(os.getenv('CHANNEL_ID')) if os.getenv('CHANNEL_ID') else -100123456789 

if not BOT_TOKEN:
    print("❌ Error: BOT_TOKEN not found in environment variables!")
    sys.exit(1)

bot = telebot.TeleBot(BOT_TOKEN)

# ۲. هندلر هوشمند برای کپی کردن تمام انواع پیام‌ها
@bot.message_handler(func=lambda message: True)
def copy_to_channel(message):
    try:
        # استفاده از copy_message به جای forward_message
        # این متد تمام محتوا (عکس، ویدیو، متن، کپشن) را دقیقاً کپی می‌کند
        bot.copy_message(
            chat_id=CHANNEL_ID, 
            from_chat_id=message.chat.id, 
            message_id=message.message_id
        )
        print(f"✅ Message (Type: {message.content_type}) copied from {message.chat.id} to {CHANNEL_ID}")
        
    except Exception as e:
        print(f"⚠️ Error during copying: {e}")

# ۳. اجرای اصلی ربات
def run_bot():
    print(f"🚀 Bot is starting... Targeting Channel: {CHANNEL_ID}")
    while True:
        try:
            bot.infinity_polling(timeout=60, long_polling_timeout=60)
        except Exception as e:
            print(f"⚠️ Connection error: {e}")
            print("⏳ Restarting in 10 seconds...")
            time.sleep(10)

if __name__ == "__main__":
    print("✅ Bot script initialized successfully.")
    run_bot()
