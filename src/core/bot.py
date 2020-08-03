import telebot
import time
import os
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv('TOKEN')

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def send_message(message):
    bot.reply_to(message, 'Welcome!')

bot.polling()