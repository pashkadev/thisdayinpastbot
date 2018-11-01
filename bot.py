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



#@bot.message_handler(commands=['start', 'go'])
#def start_handler(message):
bot.send_message(chat_id='202906676', text="I'm up and running")
#bot.send_message(chat_id='202906676', texty.check_token())
bot.send_message(chat_id='202906676', text="https://yadi.sk/d/PJTlsclG3aTguX")
bot.send_photo(chat_id='202906676', photo='https://d1nhio0ox7pgb.cloudfront.net/_img/g_collection_png/standard/512x512/robot.png')


bot.polling()