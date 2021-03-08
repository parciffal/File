import telebot
from telebot import types
import database
from config import *

bot = telebot.TeleBot(token=TOKEN)
db = database.DataConnector()


@bot.callback_query_handler(func=lambda call: call.data in ['showusers', 'sendmess'])
def callback_inline(call):
    try:
        if call.data == 'showusers':
            users = db.get_users_rows()
            string = ''
            for user in users:
                string = string + '\n' + user['name'] + ',' + user['id'] + ',' + user['status']
        elif call.data == 'sendmess':
            bot.send_message(ADMINID, 'What shell i send')

            @bot.message_handler(content_types='text')
            def everyone(message):
                ids = db.get_all_ids()
                for i in ids:
                    bot.send_message(i, message.text)
    except Exception as e:
        print(repr(e))


@bot.message_handler(commands=['start'])
def starting(message):
    if message.from_user.id == ADMINID:
        try:
            markup = types.InlineKeyboardMarkup()
            showallusers = types.InlineKeyboardButton('Show all users', callback_data='showusers')
            sendmessage = types.InlineKeyboardButton('Send message to all users', callback_data='sendmess')
            markup.add(showallusers)
            markup.add(sendmessage)
            bot.send_message(message.chat.id, 'Hello coach what we shell do today', reply_markup=markup)
        except Exception as e:
            print(repr(e))


bot.polling(none_stop=True, interval=0)
