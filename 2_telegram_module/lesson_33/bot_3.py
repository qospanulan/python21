from telebot import TeleBot, types

TOKEN = '7800185758:AAEkd4LIRIDvO53CKy4Orueht8SyUJNgxBo'

bot = TeleBot(token=TOKEN)

movies = [
    {"title": "test1", "url": "https://test1.com/"},
    {"title": "test2", "url": "https://test2.com/"},
    {"title": "test3", "url": "https://test3.com/"},
    {"title": "test4", "url": "https://test4.com/"},
    {"title": "test5", "url": "https://test5.com/"}
]


@bot.message_handler(commands=['start'])
def start_handler(msg):
    markup = types.InlineKeyboardMarkup(row_width=8)

    kbs = []
    for movie in movies:
        kb_btn = types.InlineKeyboardButton(
            text=movie['title'],
            callback_data=movie['title'],
            url=movie['url']
        )
        kbs.append(kb_btn)

    markup.add(*kbs)


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

