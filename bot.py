# -*- coding: utf-8 -*-
import telebot
import os
#import constant

#main variables
token = os.environ[TELEGRAM_TOKEN]
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, "I'm up and runnig")


bot.polling()