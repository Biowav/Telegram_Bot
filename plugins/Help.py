from utils import *

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,help_message)
