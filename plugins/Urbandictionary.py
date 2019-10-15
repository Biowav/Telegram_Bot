from utils import *
import json
def test_urbandictionary(message):
    if message.text:
        return message.text[:4]=='!ud '

@bot.message_handler(func =test_urbandictionary)
def urban_dict(message):
    text = json.loads(requests.get(
        url='http://api.urbandictionary.com/v0/define',params={'term':message.text[4:]}).text)

    #text = json.loads(requests.get('http://api.urbandictionary.com/v0/define?term=ander').text)
    if 'list' in text:
        if len(text['list'])>0:

            definition = text['list'][00]['definition']
            example=text['list'][00]['example']
            bot.send_message(message.chat.id,'<b>Definition:</b>\n'+definition+'\n\n<b>Example:</b>\n' + example,parse_mode='HTML')
    pass