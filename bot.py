import os
import telebot
import time
import sys

# ۱. دریافت تنظیمات
BOT_TOKEN = os.getenv('BOT_TOKEN')
raw_channel_id = os.getenv('CHANNEL_ID')

if not BOT_TOKEN or not raw_channel_id:
    print("❌ Error: BOT_TOKEN or CHANNEL_ID not found!")
    sys.exit(1)

# تبدیل آیدی به عدد
try:
    CHANNEL_ID = int(raw_channel_id)
except ValueError:
    print(f"❌ Error: CHANNEL_ID ({raw_channel_id}) is not a valid number!")
    sys.exit(1)

bot = telebot.TeleBot(BOT_TOKEN)

# تابع کمکی برای جلوگیری از تکرار کد
def safe_copy(message):
    try:
        bot.copy_message(CHANNEL_ID, message.chat.id, message.message_id)
        print(f"✅ Copied {message.content_type} from {message.chat.id}")
    except Exception as e:
        print(f"⚠️ Error copying {message.content_type}: {e}")

# ۲. تعریف هندلرهای اختصاصی برای انواع پیام‌ها

# برای پیام‌های متنی
@bot.message_handler(content_types=['text'])
def handle_text(message):
    safe_copy(message)

# برای عکس‌ها (همراه با کپشن)
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    safe_copy(message)

# برای ویدیوها (همراه با کپشن)
@bot.message_handler(content_types=['video'])
def handle_video(message):
    safe_copy(message)

# برای فایل‌ها/مستندات (Document)
@bot.message_handler(content_types=['document'])
def handle_document(message):
    safe_copy(message)

# برای صوت‌ها (Audio)
@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    safe_copy(message)

# برای ویدیوهای کوتاه (Animation/GIF)
@bot.message_handler(content_types=['animation'])
def handle_animation(message):
    safe_copy(message)

# برای استیکرها
@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    safe_copy(message)

# برای موقعیت مکانی و غیره (در صورت نیاز)
@bot.message_handler(content_types=['location', 'contact'])
def handle_other(message):
    safe_copy(message)

# ۳. اجرای اصلی
def run_bot():
    print(f"🚀 Bot is running... Target Channel: {CHANNEL_ID}")
    while True:
        try:
            bot.infinity_polling(timeout=60, long_polling_timeout=60)
        except Exception as e:
            print(f"⚠️ Connection error: {e}. Restarting in 10s...")
            time.sleep(10)

if __name__ == "__main__":
    run_bot()
