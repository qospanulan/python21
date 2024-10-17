from telebot import TeleBot, types

TOKEN = '7800185758:AAEkd4LIRIDvO53CKy4Orueht8SyUJNgxBo'

bot = TeleBot(token=TOKEN)


@bot.message_handler(func=lambda msg: "привет" in msg.text and "бот" in msg.text)
def func_handler(msg):
    # if "привет" in msg.text and "бот" in msg.text:
    bot.reply_to(
        message=msg,
        text=f"Привет привет!"
    )


bot.infinity_polling()
