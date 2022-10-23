import telebot
from telebot import types


bot = telebot.TeleBot('5658742630:AAEcKGRrbwO5lOUqZOuUtysUBRujppLWqw4')

@bot.message_handler(commands = ['w'])
def start(message):
    bot.send_message(message.chat.id, '<b>Привет</b>', parse_mode='html')


@bot.message_handler(commands = ['web'])
def draw_board(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Нажми', url='https://pypi.org/project/pyTelegramBotAPI'))
    bot.send_message(message.chat.id,'Перейдите', reply_markup=markup)

@bot.message_handler(commands = ['Game'])
def draw_board(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    key1 = types.KeyboardButton('1')
    key2 = types.KeyboardButton('2')
    key3 = types.KeyboardButton('3')
    key4 = types.KeyboardButton('4')
    key5 = types.KeyboardButton('5')
    key6 = types.KeyboardButton('6')
    key7 = types.KeyboardButton('7')
    key8 = types.KeyboardButton('8')
    key9 = types.KeyboardButton('9')    

    markup.add(key1, key2, key3, key4, key5, key6, key7, key8, key9)
    bot.send_message(message.chat.id,'Сделайте ход', reply_markup=markup)


bot.polling(none_stop=True)