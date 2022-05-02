from asyncio import constants
from email import message
import requests
import json
import telebot
import time
import constants

tb = telebot.TeleBot(constants.token) #ENTER YOUR BOT TOKEN FROM THE BOTFATHER

chatid = constants.chatid #ENTER YOUR CHAT ID
notify = 0

while True:
    response = requests.post('https://api.minerstat.com/v2/coins?list=FLUX')

    print(response)

    data = response.json()

    flux_difficulty = data[0]['difficulty']
    print(flux_difficulty)
    
    if flux_difficulty > 35000 and notify == 0:
        tb.send_message(chat_id=-623083544, text=f'ETH APE - flux difficulty has risen to {flux_difficulty}')
        notify = notify + 1
    elif flux_difficulty < 30000 and flux_difficulty > 25000 and notify == 1:
        tb.send_message(chat_id=-623083544, text=f'COOLING OFF - flux difficulty has fallen to {flux_difficulty}, 2 rigs FLUX')
        notify = notify - 1
    elif flux_difficulty < 25000 and notify == 0:
        tb.send_message(chat_id=-623083544, text=f'FLUX APE - flux difficulty has fallen to {flux_difficulty}')
        notify = notify + 1

    @tb.message_handler(commands=['start', 'help', 'live'])
    def send_welcome(message):
        tb.reply_to(message, "Yeargh, I'm ready to go")

    time.sleep(60)
