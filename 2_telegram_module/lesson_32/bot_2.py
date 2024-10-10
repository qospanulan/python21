import telebot

TOKEN = '7800185758:AAEkd4LIRIDvO53CKy4Orueht8SyUJNgxBo'

bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(content_types=["document"])
def start_handler(msg):
    file_id = msg.document.file_id

    file_info = bot.get_file(file_id)
    print(file_info.file_path)
    downloaded_file_binary = bot.download_file(file_info.file_path)

    with open(f'downloads/{msg.document.file_name}', 'wb') as f:
        f.write(downloaded_file_binary)

    # with open(f'downloads/{msg.document.file_name}', 'rb') as f:
    bot.send_document(
        chat_id=msg.chat.id,
        document=file_id
    )


bot.infinity_polling()
