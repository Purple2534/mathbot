import telebot
import config

from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)
 
@bot.message_handler(commands=['start'])
def welcome(message):

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Открыть дополнительные материалы")
    item2 = types.KeyboardButton("Купить МГ")
 
    markup.add(item1, item2)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы подготовить тебя к успешной сдаче ЕГЭ.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Открыть дополнительные материалы':

        	markup = types.InlineKeyboardMarkup(row_width=5)
        	item1 = types.InlineKeyboardButton("1", callback_data='1')
        	item2 = types.InlineKeyboardButton("2", callback_data='2')
        	item3 = types.InlineKeyboardButton("3", callback_data='3')
        	item4 = types.InlineKeyboardButton("4", callback_data='4')
        	item5 = types.InlineKeyboardButton("5", callback_data='5')
        	item6 = types.InlineKeyboardButton("6", callback_data='6')
        	item7 = types.InlineKeyboardButton("7", callback_data='7')
        	item8 = types.InlineKeyboardButton("8", callback_data='8')
        	item9 = types.InlineKeyboardButton("9", callback_data='9')
        	item10 = types.InlineKeyboardButton("10", callback_data='10')
        	item11 = types.InlineKeyboardButton("11", callback_data='11')
        	item12 = types.InlineKeyboardButton("12", callback_data='12')
        	

        	markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)

        	bot.send_message(message.chat.id, 'Какое задание?', reply_markup=markup)

            
        elif message.text == 'Купить МГ':
 
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 =  url_button = types.InlineKeyboardButton(text="Купить МГ", url="https://egehackplatform.ru/web/shop/43/")
 
            markup.add(item1)
 
            bot.send_message(message.chat.id, 'Нажми на кнопку', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, '1')
            elif call.data == '1':
            	with open('rolik/vidos.mp4', 'rb') as video:
                    bot.send_video(call.message.chat.id, video)
            elif call.data == '2':
                bot.send_message(call.message.chat.id, '3')
            elif call.data == '3':
            	bot.send_message(call.message.chat.id, '4')
            elif call.data == '4':
            	bot.send_message(call.message.chat.id, '5')
            elif call.data == '5':
            	bot.send_message(call.message.chat.id, '6')
            elif call.data == '6':
            	bot.send_message(call.message.chat.id, '7')
            elif call.data == '7':
            	bot.send_message(call.message.chat.id, '8')
            elif call.data == '8':
            	bot.send_message(call.message.chat.id, '9')
            elif call.data == '9':
            	bot.send_message(call.message.chat.id, '10')
            elif call.data == '10':
            	bot.send_message(call.message.chat.id, '11')
            elif call.data == '11':
            	bot.send_message(call.message.chat.id, '12')
            elif call.data == '12':
            	bot.send_message(call.message.chat.id, '13')

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
