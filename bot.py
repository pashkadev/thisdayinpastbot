# -*- coding: utf-8 -*-
import telebot
from telebot import apihelper
import os
# import constant
import yadisk
import datetime

# main variables
token = os.environ['TELEGRAM_TOKEN']

# apihelper.proxy = {'https':'socks5h://kmk.me.uk:3105'}

# token = constant.TELEGRAM_TOKEN
bot = telebot.TeleBot(token)

y = yadisk.YaDisk(token=os.environ['YADISK_TOKEN'])# constant.YADISK_TOKEN)

# @bot.message_handler(commands=['start', 'go'])
# def start_handler(message):
bot.send_message(chat_id='202906676', text="I'm up and running")
bot.send_message(chat_id='202906676', text=str(datetime.datetime.now().strftime("%d.%m.%Y %H.%M.%S")))
