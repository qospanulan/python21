import telebot

TOKEN = '7800185758:AAEkd4LIRIDvO53CKy4Orueht8SyUJNgxBo'

bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def start_handler(msg):
    bot.send_message(chat_id=msg.chat.id, text=f"Привет привет! Добро пожаловать на наш бот!")


@bot.message_handler(commands=['help'])
def help_handler(msg):
    bot.send_message(chat_id=msg.chat.id, text=f"Нужна помощь?")


@bot.message_handler(func=lambda msg: 'привет' in msg.text.lower())
def func_handler(msg):
    # bot.send_message(chat_id=msg.chat.id, text=f"Привееет!")
    bot.reply_to(
        message=msg,
        text=f"Привееет!"
    )


@bot.message_handler(content_types=['text'])
def repeat_all_messages(msg):
    print("принял какое то сообщение")
    # print(type(msg))
    # print(msg)

    print(msg.text)
    bot.send_message(chat_id=msg.chat.id, text=f"принял сообщение: {msg.text}")


bot.infinity_polling()







