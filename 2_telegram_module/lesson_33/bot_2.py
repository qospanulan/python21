from telebot import TeleBot, types

TOKEN = '7800185758:AAEkd4LIRIDvO53CKy4Orueht8SyUJNgxBo'

bot = TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def start_handler(msg):
    markup = types.InlineKeyboardMarkup(row_width=8)
    kb_1 = types.InlineKeyboardButton(
        text="Кнопка 1",
        callback_data='btn1',
        url="https://gidonline.com/mclksdc/21_film_url"
    )
    kb_2 = types.InlineKeyboardButton(text="Кнопка 2", callback_data='btn2')
    kb_3 = types.InlineKeyboardButton(text="Кнопка 3", callback_data='btn3')

    markup.add(kb_1, kb_2, kb_3)

    bot.send_message(
        chat_id=msg.chat.id,
        text="Привет привет! Добро пожаловать на наш бот!",
        reply_markup=markup
    )


@bot.callback_query_handler()
def callback_handler(callback):
    print(type(callback))
    print(callback.data)
    bot.answer_callback_query(
        callback.id,
        text=f"вы ответили правильно! +1 балл!",
        show_alert=True
    )

    bot.send_message(
        chat_id=callback.message.chat.id,
        text=f"Вы нажали на кнопку '{callback.data}'!"
    )


bot.infinity_polling()
