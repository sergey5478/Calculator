import telebot
from telebot import types

def Token():
    with open('token.txt', 'r') as data:
        token = ''
        for line in data:
            token += line        
    return token

bot = telebot.TeleBot(Token())

@bot.message_handler(commands = ['start'])
def start(message):
    mess = f'Привет! <b>{message.from_user.first_name} <u> {message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode = 'html')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):    
    bot.send_message(message.chat.id, "Best photo")
    
@bot.message_handler(commands=['website'])
def website(message): 
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Welcome", url="https://qna.habr.com/q/1143158")) 
    bot.send_message(message.chat.id, "Go website", reply_markup=markup)

@bot.message_handler(commands=['help1'])
def website(message): 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 2)
    website = types.KeyboardButton('website')
    start1 = types.KeyboardButton('Start')
    markup.add(website, start1) 
    bot.send_message(message.chat.id, 'Go website', reply_markup=markup)

bot.polling(none_stop = True)
