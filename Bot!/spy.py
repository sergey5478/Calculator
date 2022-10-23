from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime

async def log(update: Update, context: ContextTypes):
    file = open('db1.csv', 'w')
    file.write(f'{update.effective_user.first_name}, \
        {datetime.datetime.now().time()}, {update.message.text}\n')
    file.close()    