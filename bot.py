import os
import telebot
import time
import sys

# ۱. تنظیمات
BOT_TOKEN = os.getenv('BOT_TOKEN')
raw_channel_id = os.getenv('CHANNEL_ID')

if not BOT_TOKEN or not raw_channel_id:
    print("❌ Error: BOT_TOKEN or CHANNEL_ID not found!")
    sys.exit(1)

try:
    CHANNEL_ID = int(raw_channel_id)
except ValueError:
    print(f"❌ Error: CHANNEL_ID ({raw_channel_id}) is not a valid number!")
    sys.exit(1)

bot = telebot.TeleBot(BOT_TOKEN)

# ۲. تابع اصلی برای فوروارد کردن
def fast_forward(message):
    try:
        # استفاده از forward_message باعث می‌شود تلگرام خودش بنویسد "Forwarded from..."
        # و تمام محتوا (عکس، ویدیو، فایل و ...) را هم با کیفیت اصلی منتقل کند.
        bot.forward_message(CHANNEL_ID, message.chat.id, message.message_id)
        print(f"✅ Forwarded {message.content_type} from {message.chat.id}")
    except Exception as e:
        print(f"⚠️ Error forwarding {message.content_type}: {e}")

# ۳. تعریف هندلرهای اختصاصی برای انواع محتوا
# ما از لیست تمام content_types استفاده می‌کنیم تا هیچ پیامی رد نشود

# این لیست شامل تمام انواع پیام‌هایی است که ممکن است دریافت کنید
ALL_CONTENT_TYPES = [
    'text', 'photo', 'video', 'document', 'audio', 
    'sticker', 'animation', 'location', 'contact', 'voice'
]

# به جای نوشتن تک تک، با یک حلقه هندلرها را برای همه تعریف می‌کنیم
for content in ALL_CONTENT_TYPES:
    @bot.message_handler(content_types=[content])
    def handler(message, content_type=content):
        fast_forward(message)

# ۴. اجرای ربات
def run_bot():
    print(f"🚀 Bot is starting... Forwarding all content to: {CHANNEL_ID}")
    while True:
        try:
            bot.infinity_polling(timeout=60, long_polling_timeout=60)
        except Exception as e:
            print(f"⚠️ Connection error: {e}. Restarting in 10s...")
            time.sleep(10)

if __name__ == "__main__":
    run_bot()
