from telebot import TeleBot, types

TOKEN = '7800185758:AAEkd4LIRIDvO53CKy4Orueht8SyUJNgxBo'

bot = TeleBot(token=TOKEN)


@bot.message_handler(commands=['get_echo'])
def func_handler(msg):
    text_to_echo_words = msg.text.split(' ')[1:]
    text_to_echo = ' '.join(text_to_echo_words)
    bot.send_message(
        chat_id=msg.chat.id,
        text=f"echo: {text_to_echo}"
    )


@bot.message_handler(commands=['test'])
def func_handler(msg):
    bot.send_message(
        chat_id=msg.chat.id,
        text=f"Тестовое сообщение!"
    )

    # bot.reply_to(
    #     message=msg,
    #     text=f"echo: '{msg.text}'"
    # )


bot.infinity_polling()

