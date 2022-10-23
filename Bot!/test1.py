import telebot
from telebot import types

bot = telebot.TeleBot('5658742630:AAEcKGRrbwO5lOUqZOuUtysUBRujppLWqw4')

board = ['1','2','3','4','5','6','7','8','9']

@bot.message_handler(commands = ['Game'])
def draw_board(message):     
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)    
    key1 = types.KeyboardButton(board[0])
    key2 = types.KeyboardButton(board[1])
    key3 = types.KeyboardButton(board[2])
    key4 = types.KeyboardButton(board[3])
    key5 = types.KeyboardButton(board[4])
    key6 = types.KeyboardButton(board[5])
    key7 = types.KeyboardButton(board[6])
    key8 = types.KeyboardButton(board[7])
    key9 = types.KeyboardButton(board[8])    

    markup.add(key1, key2, key3, key4, key5, key6, key7, key8, key9)
    bot.send_message(message.chat.id,'Сделайте ход', reply_markup=markup)
bot.polling(none_stop=True)

@bot.message_handler(commands = ['1','2','3','4','5','6','7','8','9'])
def numbes 

# def check_win(board):
#     win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),\
#         (0,4,8),(2,4,6))
#     for w in win_coord:        
#         if board[w[0]] == board[w[1]] == board[w[2]]:            
#             return board[w[0]]
#     return False

