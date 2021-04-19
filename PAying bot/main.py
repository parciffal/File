from aiogram.bot import Bot
from aiogram.dispatcher import Dispatcher
from config import *
import logging
from aiogram import types, executor
from time import sleep

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.callback_query_handler(lambda call: call.data in ['payweek', 'paymonth', 'payyear'])
async def call_two(call):
    try:
        if call.data == 'payweek':
            markup = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton('💳 Subscribe', url=PAY_LINK_WEEK)
            markup.add(b1)
            mess = await bot.send_message(call.message.chat.id, 'Click the button below:', reply_markup=markup)
            sleep(5)
            await bot.delete_message(call.message.chat.id, message_id=mess.message_id)
        elif call.data == 'paymonth':
            markup = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton('💳 Subscribe', url=PAY_LINK_MONTH)
            markup.add(b1)
            mess = await bot.send_message(call.message.chat.id, 'Click the button below:', reply_markup=markup)
            sleep(5)
            await bot.delete_message(call.message.chat.id, message_id=mess.message_id)
        elif call.data == 'payyear':
            markup = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton('💳 Subscribe', url=PAY_LINK_YEAR)
            markup.add(b1)
            mess = await bot.send_message(call.message.chat.id, 'Click the button below:', reply_markup=markup)
            sleep(5)
            await bot.delete_message(call.message.chat.id, message_id=mess.message_id)

    except Exception as e:
        print(repr(e))


@dp.callback_query_handler(lambda call: call.data in ['week', 'month', 'year', 'back'])
async def call_one(call):
    try:
        if call.data == 'week':
            markup = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton('💳 Credit/Debit Card', callback_data='payweek')
            b2 = types.InlineKeyboardButton('<< Back', callback_data='back')
            markup.add(b1)
            markup.add(b2)
            await bot.edit_message_text('Weekly\n'
                                        '\n'
                                        'Your benefits:\n'
                                        '✅ TradingFX Bot (Access to the channel)\n'
                                        '\n'
                                        'Price: $10.00\n'
                                        'Billing period:1 week\n'
                                        'Billing mode: recurring\n',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id
                                        , reply_markup=markup)
        elif call.data == 'month':
            markup = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton('💳 Credit/Debit Card', callback_data='paymonth')
            b2 = types.InlineKeyboardButton('<< Back', callback_data='back')
            markup.add(b1)
            markup.add(b2)
            await bot.edit_message_text('Monthly\n'
                                        '\n'
                                        'Your benefits:\n'
                                        '✅ TradingFX Bot (Access to the channel)\n'
                                        '\n'
                                        'Price: $20.00\n'
                                        'Billing period:1 month\n'
                                        'Billing mode: recurring\n',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id
                                        , reply_markup=markup)
        elif call.data == 'year':
            markup = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton('💳 Credit/Debit Card', callback_data='payyear')
            b2 = types.InlineKeyboardButton('<< Back', callback_data='back')
            markup.add(b1)
            markup.add(b2)
            await bot.edit_message_text('Yearly\n'
                                        '\n'
                                        'Your benefits:\n'
                                        '✅ TradingFX Bot (Access to the channel)\n'
                                        '\n'
                                        'Price: $150.00\n'
                                        'Billing period:1 year\n'
                                        'Billing mode: recurring\n',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id
                                        , reply_markup=markup)
        elif call.data == 'back':
            markup = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton('Weekly, $10.00/1 week', callback_data='week')
            b2 = types.InlineKeyboardButton('Monthly $20/1 month', callback_data='month')
            b3 = types.InlineKeyboardButton('Yearly $150/1 year', callback_data='year')
            markup.add(b1)
            markup.add(b2)
            markup.add(b3)
            await bot.edit_message_text('💥SimpleTrading FX SIGNALS AND ANALYSIS 💥\n\n'
                                        '📈Daily Signals\n'
                                        '📉Markups with analysis included\n'
                                        '📈Step by Step Updates\n'
                                        '📉 All Trades I’m taking!\n'
                                        '📉TP & SL always included\n'
                                        '\n'
                                        '✖️Cancel subscription anytime ✖️\n'
                                        '\n'
                                        '\n'
                                        'Pay Attention to the numbers #️⃣\n'
                                        '\n'
                                        'Try to be quick 💨\n'
                                        '\n'
                                        'Risk only 1-3% per trade 🔥\n'
                                        '\n'
                                        'Let’s get this Bread 😈\n'
                                        '\n'
                                        '\n'
                                        '❌ No refunds ❌\n'
                                        '\n'
                                        'Please do not share any content\n'
                                        'from this group‼\n'
                                        '\n'
                                        'MOST IMPORTANTLY DO NOT RISK \n'
                                        'MORE THAN 1-3% 🔑\n'
                                        '\n'
                                        'Please select your subscription plan:',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=markup)
    except Exception as e:
        print(repr(e))


@dp.message_handler(commands=['start', 'Plans'])
async def hello(message: types.Message):
    try:
        markup = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton('Weekly, $10.00/1 week', callback_data='week')
        b2 = types.InlineKeyboardButton('Monthly $20/1 month', callback_data='month')
        b3 = types.InlineKeyboardButton('Yearly $150/1 year', callback_data='year')
        markup.add(b1)
        markup.add(b2)
        markup.add(b3)
        await bot.send_message(message.chat.id, 'Hi {username}'.format(username=message.from_user.username))
        await bot.send_message(message.chat.id, '💥SimpleTrading FX SIGNALS AND ANALYSIS 💥\n\n'
                                                '📈Daily Signals\n'
                                                '📉Markups with analysis included\n'
                                                '📈Step by Step Updates\n'
                                                '📉 All Trades I’m taking!\n'
                                                '📉TP & SL always included\n'
                                                '\n'
                                                '✖️Cancel subscription anytime ✖️\n'
                                                '\n'
                                                '\n'
                                                'Pay Attention to the numbers #️⃣\n'
                                                '\n'
                                                'Try to be quick 💨\n'
                                                '\n'
                                                'Risk only 1-3% per trade 🔥\n'
                                                '\n'
                                                'Let’s get this Bread 😈\n'
                                                '\n'
                                                '\n'
                                                '❌ No refunds ❌\n'
                                                '\n'
                                                'Please do not share any content\n'
                                                'from this group‼\n'
                                                '\n'
                                                'MOST IMPORTANTLY DO NOT RISK \n'
                                                'MORE THAN 1-3% 🔑\n'
                                                '\n'
                                                'Please select your subscription plan:', reply_markup=markup)

    except Exception as e:
        print(repr(e))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
