import database
import telebot
from telebot import types
from config import TOKEN
from config import *

bot = telebot.TeleBot(token=TOKEN)
dataconnector = database.DataConnector()


@bot.callback_query_handler(func=lambda call: call.data in ['yesone', 'yestwo', 'yesthree', 'yesfour', 'yesfive'])
def callback_inlinem(call):
    try:
        if call.message:
            if call.data == 'yesone':
                textq = str(YESVIDEO1)
                bot.send_message(call.message.chat.id, textq)
                markyes = types.InlineKeyboardMarkup()
                butt2 = types.InlineKeyboardButton('Multilevel Pyramid', callback_data='yestwo')
                butt3 = types.InlineKeyboardButton('Product', callback_data='yesthree')
                butt4 = types.InlineKeyboardButton('Multilevel Marketing (GoPro)', callback_data='yesfour')
                butt5 = types.InlineKeyboardButton('12 pillars of Jim Rohn', callback_data='yesfive')
                markyes.add(butt2)
                markyes.add(butt3)
                markyes.add(butt4)
                markyes.add(butt5)
                bot.send_message(call.message.chat.id, 'Videos for you', reply_markup=markyes)
            elif call.data == 'yestwo':
                textq = str(YESVIDEO2)
                bot.send_message(call.message.chat.id, textq)
                markyes = types.InlineKeyboardMarkup()
                butt1 = types.InlineKeyboardButton('Herbalife History', callback_data='yesone')
                butt3 = types.InlineKeyboardButton('Product', callback_data='yesthree')
                butt4 = types.InlineKeyboardButton('Multilevel Marketing (GoPro)', callback_data='yesfour')
                butt5 = types.InlineKeyboardButton('12 pillars of Jim Rohn', callback_data='yesfive')
                markyes.add(butt1)
                markyes.add(butt3)
                markyes.add(butt4)
                markyes.add(butt5)
                bot.send_message(call.message.chat.id, 'Videos for you', reply_markup=markyes)
            elif call.data == 'yesthree':
                textq = str(YESVIDEO3)
                bot.send_message(call.message.chat.id, textq)
                markyes = types.InlineKeyboardMarkup()
                butt1 = types.InlineKeyboardButton('Herbalife History', callback_data='yesone')
                butt2 = types.InlineKeyboardButton('Multilevel Pyramid', callback_data='yestwo')
                butt4 = types.InlineKeyboardButton('Multilevel Marketing (GoPro)', callback_data='yesfour')
                butt5 = types.InlineKeyboardButton('12 pillars of Jim Rohn', callback_data='yesfive')
                markyes.add(butt1)
                markyes.add(butt2)
                markyes.add(butt4)
                markyes.add(butt5)
                bot.send_message(call.message.chat.id, 'Videos for you', reply_markup=markyes)
            elif call.data == 'yesfour':
                textq = str(YESVIDEO4)
                bot.send_message(call.message.chat.id, textq)
                markyes = types.InlineKeyboardMarkup()
                butt1 = types.InlineKeyboardButton('Herbalife History', callback_data='yesone')
                butt2 = types.InlineKeyboardButton('Multilevel Pyramid', callback_data='yestwo')
                butt3 = types.InlineKeyboardButton('Product', callback_data='yesthree')
                butt5 = types.InlineKeyboardButton('12 pillars of Jim Rohn', callback_data='yesfive')
                markyes.add(butt1)
                markyes.add(butt2)
                markyes.add(butt3)
                markyes.add(butt5)
                bot.send_message(call.message.chat.id, 'Videos for you', reply_markup=markyes)
            elif call.data == 'yesfive':
                textq = str(YESVIDEO5)
                bot.send_message(call.message.chat.id, textq)
                markyes = types.InlineKeyboardMarkup()
                butt1 = types.InlineKeyboardButton('Herbalife History', callback_data='yesone')
                butt2 = types.InlineKeyboardButton('Multilevel Pyramid', callback_data='yestwo')
                butt3 = types.InlineKeyboardButton('Product', callback_data='yesthree')
                butt4 = types.InlineKeyboardButton('Multilevel Marketing (GoPro)', callback_data='yesfour')
                markyes.add(butt1)
                markyes.add(butt2)
                markyes.add(butt3)
                markyes.add(butt4)
                bot.send_message(call.message.chat.id, 'Videos for you', reply_markup=markyes)
    except Exception as e:
        print(repr(e))


@bot.callback_query_handler(func=lambda call: call.data in ['noone', 'notwo', 'nothree', 'nofour'])
def callback_inlinem(call):
    try:
        if call.message:
            if call.data == 'noone':
                textq = str(button1)
                bot.send_message(call.message.chat.id, 'From cutivation to table')
                bot.send_message(call.message.chat.id, textq)
                textq = str(button12)
                bot.send_message(call.message.chat.id, 'Introduction: Global Nutrition Philosophy')
                bot.send_message(call.message.chat.id, textq)
                textq = str(button13)
                bot.send_message(call.message.chat.id, 'Understanding Nutrition: Macro and Micronutrients')
                bot.send_message(call.message.chat.id, textq)
                textq = str(button14)
                bot.send_message(call.message.chat.id, 'HEART HEALTH')
                bot.send_message(call.message.chat.id, textq)
                textq = str(button15)
                bot.send_message(call.message.chat.id, 'Dra Rocio Medina: Importance of breakfastmm')
                bot.send_message(call.message.chat.id, textq)
                markno = types.InlineKeyboardMarkup()

                butt2 = types.InlineKeyboardButton('I want to know more about busniess', callback_data='notwo')
                butt3 = types.InlineKeyboardButton('I want to know more about support tools', callback_data='notree')
                butt4 = types.InlineKeyboardButton('I want to know more about business tools', callback_data='nofour')

                markno.add(butt2)
                markno.add(butt3)
                markno.add(butt4)
                bot.send_message(call.message.chat.id, 'Watch this videos', reply_markup=markno)
            elif call.data == 'notwo':
                textq = str(button21)
                bot.send_message(call.message.chat.id, 'First Steps in Business')
                bot.send_message(call.message.chat.id, textq)
                textq = str(button22)
                bot.send_message(call.message.chat.id, 'Goal and Plan and Action')
                bot.send_message(call.message.chat.id, textq)
                textq = str(button23)
                bot.send_message(call.message.chat.id, 'Marketing Plan with Edgar Balbás- Spanish')
                bot.send_message(call.message.chat.id, textq)
                textq = str(button24)
                bot.send_message(call.message.chat.id, 'How do you make money? Jhon Tartol- Club Chairmans Plan 1')
                bot.send_message(call.message.chat.id, textq)
                textq = str(button25)
                bot.send_message(call.message.chat.id, ' How do you make money? Jhon Tartol- Club Chairmans Plan 2')
                bot.send_message(call.message.chat.id, textq)
                textq = str(button26)
                bot.send_message(call.message.chat.id, 'How to make a Product presentation?')
                bot.send_message(call.message.chat.id, textq)
                textq = str(button27)
                bot.send_message(call.message.chat.id, 'How to use HOM?')
                bot.send_message(call.message.chat.id, textq)
                textq = str(button28)
                bot.send_message(call.message.chat.id, 'How to do a VIRTUAL Health Assessment')
                bot.send_message(call.message.chat.id, textq)
                textq = str(button29)
                bot.send_message(call.message.chat.id, 'Advance with 21 Day Challenges')
                bot.send_message(call.message.chat.id, textq)
                textq = str(button210)
                bot.send_message(call.message.chat.id, 'Online registration process for people')
                bot.send_message(call.message.chat.id, textq)
                markno = types.InlineKeyboardMarkup()

                butt1 = types.InlineKeyboardButton('I want to know more about the product', callback_data='noone')
                butt3 = types.InlineKeyboardButton('I want to know more about support tools', callback_data='notree')
                butt4 = types.InlineKeyboardButton('I want to know more about business tools', callback_data='nofour')
                markno.add(butt1)
                markno.add(butt3)
                markno.add(butt4)
                bot.send_message(call.message.chat.id, 'Watch this videos', reply_markup=markno)
            elif call.data == 'nothree':
                textq = str(button31)
                bot.send_message(call.message.chat.id, 'Recruitment Tools')
                bot.send_message(call.message.chat.id, textq)
                textq = str(button32)
                bot.send_message(call.message.chat.id, 'Tutorial : This is Herbalife Nutrition!')
                bot.send_message(call.message.chat.id, textq)
                textq = str(button33)
                bot.send_message(call.message.chat.id, 'How to expand your list on Social Networks?')
                bot.send_message(call.message.chat.id, textq)
                markno = types.InlineKeyboardMarkup()
                butt1 = types.InlineKeyboardButton('I want to know more about the product', callback_data='noone')
                butt2 = types.InlineKeyboardButton('I want to know more about busniess', callback_data='notwo')
                butt4 = types.InlineKeyboardButton('I want to know more about business tools', callback_data='nofour')
                markno.add(butt1)
                markno.add(butt2)
                markno.add(butt4)
                bot.send_message(call.message.chat.id, 'Watch this videos', reply_markup=markno)
            elif call.data == 'nofour':
                textq = str(button41)
                bot.send_message(call.message.chat.id, 'Business Tools')
                bot.send_message(call.message.chat.id, textq)
                textq = str(button42)
                bot.send_message(call.message.chat.id, 'How to order at Myherbalife SAMCAM')
                bot.send_message(call.message.chat.id, textq)
                textq = str(button43)
                bot.send_message(call.message.chat.id, 'How to order oline directly to the customer in USA?')
                bot.send_message(call.message.chat.id, textq)
                markno = types.InlineKeyboardMarkup()
                butt1 = types.InlineKeyboardButton('I want to know more about the product', callback_data='noone')
                butt2 = types.InlineKeyboardButton('I want to know more about busniess', callback_data='notwo')
                butt3 = types.InlineKeyboardButton('I want to know more about support tools', callback_data='notree')

                markno.add(butt1)
                markno.add(butt2)
                markno.add(butt3)

                bot.send_message(call.message.chat.id, 'Watch this videos', reply_markup=markno)
    except Exception as e:
        print(repr(e))


@bot.callback_query_handler(func=lambda call: call.data in ['yes', 'no'])
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'yes':
                markyes = types.InlineKeyboardMarkup()
                butt1 = types.InlineKeyboardButton('Herbalife History', callback_data='yesone')
                butt2 = types.InlineKeyboardButton('Multilevel Pyramid', callback_data='yestwo')
                butt3 = types.InlineKeyboardButton('Product', callback_data='yesthree')
                butt4 = types.InlineKeyboardButton('Multilevel Marketing (GoPro)', callback_data='yesfour')
                butt5 = types.InlineKeyboardButton('12 pillars of Jim Rohn', callback_data='yesfive')
                markyes.add(butt1)
                markyes.add(butt2)
                markyes.add(butt3)
                markyes.add(butt4)
                markyes.add(butt5)
                bot.send_message(call.message.chat.id, 'Videos for you', reply_markup=markyes)
            elif call.data == 'no':
                markno = types.InlineKeyboardMarkup()
                butt1 = types.InlineKeyboardButton('I want to know more about the product', callback_data='noone')
                butt2 = types.InlineKeyboardButton('I want to know more about busniess', callback_data='notwo')
                butt3 = types.InlineKeyboardButton('I want to know more about support tools', callback_data='notree')
                butt4 = types.InlineKeyboardButton('I want to know more about business tools', callback_data='nofour')
                markno.add(butt1)
                markno.add(butt2)
                markno.add(butt3)
                markno.add(butt4)
                bot.send_message(call.message.chat.id, 'Watch this videos', reply_markup=markno)

    except Exception as e:
        print(repr(e))


@bot.message_handler(commands=['subscribe'])
def subscribe(message):
    id = message.from_user.id
    dataconnector.make_userActive(id)
    bot.send_message(message.chat.id, 'You succesfully Subscribed')


@bot.message_handler(commands=['unsubscribe'])
def unsubscribe(message):
    id = message.from_user.id
    dataconnector.make_userNotActive(id)
    bot.send_message(message.chat.id, "You sudenly Unsubscribed")


@bot.message_handler(commands=['start'])
def start_message(message):
    butt1 = types.KeyboardButton('/subscribe')
    butt2 = types.KeyboardButton('/unsubscribe')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=4)
    markup.add(butt1,butt2)
    dataconnector.add_user(message.from_user.username, message.from_user.id, False)
    bot.send_message(message.chat.id, ("Welcome {username}.\n I am the Assistant Bot of Lifetimeteam, "
                                       " where we will guide you step by step how to take your first steps,"
                                       "  together withg your sponsor and with the virtual system, "
                                       " to progress month by month and achieve the goals you set for yourself in the deal").format(
        username=message.from_user.username), reply_markup=markup)
    butt_yes = types.InlineKeyboardButton("Yes", callback_data='yes')
    butt_no = types.InlineKeyboardButton("No", callback_data='no')
    markup1 = types.InlineKeyboardMarkup(row_width=3)
    markup1.add(butt_yes, butt_no)
    bot.send_message(message.chat.id, 'Lets get started!!! Are you a new Distributor', reply_markup=markup1)


bot.polling(none_stop=True, interval=0)
