from utils import *
import listener
import json
import re


def test_bible(message):
    if message.text:
        return message.text[:3] == '!b '


@bot.message_handler(func=test_bible)
def bible(message):
    holy_words = message.text.split()
    try:
        holy_text = requests.post('https://getbible.net/json?p={0}{1}'.format(holy_words[1], holy_words[2])).content.decode()
        god_words = json.loads(holy_text[1:(len(holy_text)-2)])
        holy_aux=god_words['book'][0]['chapter']
        key, value = list(holy_aux.items())[0]
        final_words= value['verse']
        bot.send_message(message.chat.id, final_words)
    except:
        bot.send_message(message.chat.id, 'No encuentro el pasaje')