import os
import random
import sys

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

import word as wo

def getToken():
    token = ''
    if os.path.isfile(wo.TOKEN):
        f = open(wo.TOKEN, "r")
        token = f.read()
        f.close()
    else:
        sys.exit()  
    return token

def isWin(arr, who):
    if (((arr[0] == who) and (arr[4] == who) and (arr[8] == who)) or
            ((arr[2] == who) and (arr[4] == who) and (arr[6] == who)) or
            ((arr[0] == who) and (arr[1] == who) and (arr[2] == who)) or
            ((arr[3] == who) and (arr[4] == who) and (arr[5] == who)) or
            ((arr[6] == who) and (arr[7] == who) and (arr[8] == who)) or
            ((arr[0] == who) and (arr[3] == who) and (arr[6] == who)) or
            ((arr[1] == who) and (arr[4] == who) and (arr[7] == who)) or
            ((arr[2] == who) and (arr[5] == who) and (arr[8] == who))):
        return True
    return False

def countUndefinedCells(cellArray):
    counter = 0
    for i in cellArray:
        if i == wo.Undef:
            counter += 1
    return counter

def game(callBackData):    
    message = wo.Your_Turn  
    alert = None
    buttonNumber = int(callBackData[0])  
    if not buttonNumber == 9:  
        charList = list(callBackData)  
        charList.pop(0)  
        if charList[buttonNumber] == wo.Undef:  
            charList[buttonNumber] = wo.First  
            if isWin(charList, wo.First):  
                message = wo.You_Win
            else:  
                if countUndefinedCells(charList) != 0:                      
                    isCycleContinue = True                    
                    while (isCycleContinue):
                        rand = random.randint(0, 8)  
                        if charList[rand] == wo.Undef:  
                            charList[rand] = wo.Sekond
                            isCycleContinue = False  
                            if isWin(charList, wo.Sekond):  
                                message = wo.Bot_Win
        
        else:
            alert = wo.Attention        
        if countUndefinedCells(charList) == 0 and message == wo.Your_Turn:
            message = wo.Draw
        
        callBackData = ''
        for c in charList:
            callBackData += c
    
    if message == wo.You_Win or message == wo.Bot_Win or message == wo.Draw:
        message += '\n'
        for i in range(0, 3):
            message += '\n | '
            for j in range(0, 3):
                message += callBackData[j + i * 3] + ' | '
        callBackData = None  

    return message, callBackData, alert

def getKeyboard(callBackData):
    keyboard = [[], [], []]  
    if callBackData != None:          
        for i in range(0, 3):
            for j in range(0, 3):
                keyboard[i].append(InlineKeyboardButton(callBackData[j + i * 3], \
                    callback_data=str(j + i * 3) + callBackData))
    return keyboard

def newGame(update, _):
    
    data = ''
    for i in range(0, 9):
        data += wo.Undef
    
    update.message.reply_text(wo.Your_Turn, reply_markup=\
        InlineKeyboardMarkup(getKeyboard(data)))

def button(update, _):
    query = update.callback_query
    callbackData = query.data  

    message, callbackData, alert = game(callbackData)  
    if alert is None:  
        query.answer()  
        query.edit_message_text(text=message, reply_markup=InlineKeyboardMarkup(getKeyboard(callbackData)))
    else:  
        query.answer(text=alert, show_alert=True)

def help_command(update, _):
    update.message.reply_text(wo.Help)

if __name__ == '__main__':
    updater = Updater(getToken())  
    
    updater.dispatcher.add_handler(CommandHandler('start', newGame))
    updater.dispatcher.add_handler(CommandHandler('new_game', newGame))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, help_command))  
    updater.dispatcher.add_handler(CallbackQueryHandler(button))  
    
    updater.start_polling()
    updater.idle()