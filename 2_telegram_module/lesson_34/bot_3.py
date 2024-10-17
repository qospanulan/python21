from telebot import TeleBot, types

TOKEN = '7800185758:AAEkd4LIRIDvO53CKy4Orueht8SyUJNgxBo'

bot = TeleBot(token=TOKEN)


# @bot.message_handler(content_types=['new_chat_members'])
# def user_greeting(msg):
#     bot.reply_to(msg, text='Приветствуем тебя в этой замечательной группе! Если понадобится помощь, введи команду /help')


@bot.message_handler(commands=['get_admins'])
def get_admins(msg):

    admins = bot.get_chat_administrators(chat_id=msg.chat.id)
    # print(admins)
    # for admin in admins:
    #     print(admin.user.username)

    admin_usernames = "\n".join([f"@{admin.user.username}" for admin in admins])

    bot.send_message(
        chat_id=msg.chat.id,
        text=f'админы: \n{admin_usernames}')


@bot.message_handler(content_types=['new_chat_members'])
def user_greeting(msg):
    for new_member in msg.new_chat_members:
        bot.reply_to(
            msg,
            text=f'Привет, @{new_member.username}!')


bot.infinity_polling()
