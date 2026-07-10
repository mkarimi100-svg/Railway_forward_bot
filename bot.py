def safe_copy(message):
    try:
        # ۱. کپی کردن خودِ محتوا
        copied_msg = bot.copy_message(CHANNEL_ID, message.chat.id, message.message_id)
        
        # ۲. آماده‌سازی اطلاعات فرستنده
        if message.chat.type == 'private':
            # اگر پیام از پی‌وی (Private) آمده باشد
            user_info = f"👤 From: {message.chat.first_name} (@{message.chat.username})"
        elif message.chat.title:
            # اگر پیام از یک گروه/کانال دیگر آمده باشد
            user_info = f"👥 From Group/Channel: {message.chat.title}"
        else:
            user_info = f"🆔 From ID: {message.chat.id}"

        # ۳. ارسال اطلاعات فرستنده به عنوان پاسخ به همان پیام کپی شده
        # reply_to_message_id باعث می‌شود متن شما درست زیرِ عکس یا فایلی که کپی شد قرار بگیرد
        bot.send_message(
            CHANNEL_ID, 
            text=f"📌 {user_info}", 
            reply_to_message_id=copied_msg.message_id
        )
        
        print(f"✅ Copied {message.content_type} from {message.chat.id} with signature.")
        
    except Exception as e:
        print(f"⚠️ Error copying {message.content_type}: {e}")
