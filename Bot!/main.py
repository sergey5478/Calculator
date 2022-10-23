from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *
from Game import *
from Button import *


app = ApplicationBuilder().\
    token("5658742630:AAEcKGRrbwO5lOUqZOuUtysUBRujppLWqw4").build()

app.add_handler(CommandHandler("hello", hello_com))
app.add_handler(CommandHandler("time", time_com))
app.add_handler(CommandHandler("help", help_com))
app.add_handler(CommandHandler("sum", sum_com))
# app.add_handler(CommandHandler("1", draw_board1))

print('\033[32m Сервер старт \033[0m')
app.run_polling()