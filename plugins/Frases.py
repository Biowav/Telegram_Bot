from utils import *
import random
def test_edu(message):
    if message.text:
        return message.text[:4]=='!edu' and message.chat.id==-195568193

@bot.message_handler(func=test_edu)
def edu(message):
    if message.text =='!edu':
        bot.send_message(message.chat.id,random.choice(list(edu_list.values())))
    elif message.text[5:] in edu_list:
        bot.send_message(message.chat.id,edu_list[message.text[5:]])
    else:
        bot.send_message(message.chat.id,'no encuentro la frase macho')


