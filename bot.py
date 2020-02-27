# - *- coding: utf- 8 - *-
import telebot
import config
import random
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)
 
@bot.message_handler(commands=['start'])
def welcome(message):

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Случайная задача")
    item2 = types.KeyboardButton("Я сам(а) выберу задачу")
 
    markup.add(item1, item2)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы подготовить тебя к успешной сдаче ЕГЭ.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Случайная задача':
            bot.send_message(message.chat.id, str(random.randint(1,19)))
        elif message.text == 'Я сам(а) выберу задачу':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("1 Часть", callback_data='good')
            item2 = types.InlineKeyboardButton("2 Часть", callback_data='bad')
 
            markup.add(item1, item2)
 
            bot.send_message(message.chat.id, 'Из какой части?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, '1. Про­стей­шие текстовые задачи:\n-Вычисления(https://math-ege.sdamgia.ru/test?theme=174)\n-Округ­ле­ние с недостатком(https://math-ege.sdamgia.ru/test?theme=1)\n-Округление с избытком(https://math-ege.sdamgia.ru/test?theme=2)\n-Проценты(https://math-ege.sdamgia.ru/test?theme=249)\n-Проценты и округление(https://math-ege.sdamgia.ru/test?theme=5)')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, '13.Уравнения:\n-Иррациональные уравнения(https://math-ege.sdamgia.ru/test?theme=275)')
 
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Если ты решил(а) не правильно, то переходи на канал с разбором такой задачи ...",
                reply_markup=None)
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="У тебя всё получится!")
 
    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)
