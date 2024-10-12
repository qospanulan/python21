from telebot import TeleBot, types

TOKEN = '7800185758:AAEkd4LIRIDvO53CKy4Orueht8SyUJNgxBo'

bot = TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def start_handler(msg):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb_1 = types.KeyboardButton(text="Кнопка 1")
    kb_2 = types.KeyboardButton(text="Кнопка 2")

    markup.add(kb_1, kb_2)

    bot.send_message(
        chat_id=msg.chat.id,
        text=f"Привет привет! Добро пожаловать на наш бот!",
        reply_markup=markup
    )


@bot.message_handler(func=lambda msg: msg.text in ['Кнопка 1', 'Кнопка 2'])
def func_handler(msg):
    bot.reply_to(
        message=msg,
        text=f"Вы нажали на кнопку '{msg.text}'!"
    )


bot.infinity_polling()
