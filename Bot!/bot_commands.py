from telebot import types
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *
from Button import *

    
async def hello_com(update: Update, context: ContextTypes ):
    await log(update, context)
    await update.message.reply_text(f'Hello \
        {update.effective_user.first_name}')

async def time_com(update: Update, context: ContextTypes):
    await log(update, context)
    await update.message.reply_text(f'\
        {datetime.datetime.now().time()}')

async def help_com(update: Update, context: ContextTypes):
    await log(update, context)
    await update.message.reply_text(f'/Hello\n/time\n/help\n/sum')

async def sum_com(update: Update, context: ContextTypes):
    await log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')