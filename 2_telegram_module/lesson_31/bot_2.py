import telebot

TOKEN = '7800185758:AAEkd4LIRIDvO53CKy4Orueht8SyUJNgxBo'

bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(content_types=['text'])
def repeat_all_messages(msg):
    print("принял какое то сообщение")
    # print(type(msg))
    # print(msg)

    print(msg.text)
    bot.send_message(chat_id=msg.chat.id, text=msg.text)


bot.infinity_polling()


