from telebot import TeleBot, types

TOKEN = '7800185758:AAEkd4LIRIDvO53CKy4Orueht8SyUJNgxBo'

bot = TeleBot(token=TOKEN)

users = {
    '@qospan': 11111111,
    '@kospanulan': 564875397
}


@bot.message_handler(commands=['kick_user'])
def kick_user_handler(msg):
    username_to_kick = msg.text.split(' ')[1]
    print(username_to_kick)

    bot.send_message(
        chat_id=msg.chat.id,
        text=f"Мы пытаемся кикнуть {username_to_kick}! Его айди: {users[username_to_kick]}"
    )

    bot.kick_chat_member(
        chat_id=msg.chat.id,
        user_id=users[username_to_kick]
    )



@bot.message_handler(commands=['get_chat_members'])
def get_chat_members(msg):
    bot.send_message(
        chat_id=msg.chat.id,
        text=f'{users}')


@bot.message_handler(content_types=['new_chat_members'])
def user_greeting(msg):
    for new_member in msg.new_chat_members:
        users[f"@{new_member.username}"] = new_member.id
        bot.reply_to(
            msg,
            text=f'Привет, @{new_member.username}!')


bot.infinity_polling()
