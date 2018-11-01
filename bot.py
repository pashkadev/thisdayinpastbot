# -*- coding: utf-8 -*-
import telebot
from telebot import apihelper
import os
#import constant
import yadisk

#main variables
token = os.environ['TELEGRAM_TOKEN']

#apihelper.proxy = {'https':'socks5h://kmk.me.uk:3105'}

#token = constant.TELEGRAM_TOKEN
bot = telebot.TeleBot(token)

y = yadisk.YaDisk(token=os.environ['YADISK_TOKEN'])#constant.YADISK_TOKEN)



#print(y.check_token())
#print(list(y.listdir("/Photo_BACKUP")))



@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, "I'm up and running")
    bot.send_message(message.chat.id, y.check_token())
    bot.send_message(message.chat.id, list(y.listdir("/Photo_BACKUP")))


bot.polling()