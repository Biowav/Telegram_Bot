from utils import *
import datetime
markup = types.ReplyKeyboardMarkup(one_time_keyboard=False,selective=True)
#markup=types.ReplyKeyboardRemove()
'AgADBAADxKgxG6ME6VD7Swediqrc6wMXZhkABCaQ8K_aLGu4LeMCAAEC'
def search_coincidence(list1, list2):
    for word in list1:
        if word in list2:
            return word

def test_message(message):
    if message.text:
        return not ('/' in message.text[0])


def test_gauss(message):
    if message.text:
        return 'gauss' in message.text.lower()
        #return False

def test_michel(message):
    if message.text:
        return 'lo sabes' in message.text.lower()

def test_message_order(message):
    if message.text:
        return '!mensaje '==message.text[:9] and message.from_user.id!=876647460

@bot.message_handler(func=test_message_order)
def message_order(message):
    bot.send_message(-219419208,message.text[9:],parse_mode='HTML')

@bot.message_handler(func=test_michel)
def lo_sabes(message):
    bot.send_sticker(message.chat.id,'CAADBAADDAADxoFgECsXFXKslb0GAg')


@bot.message_handler(func=test_gauss)
def cleverbot_message(message):
    bot.send_message(chat_id=message.chat.id, text=cb_ask(message.text.lower().replace('gauss', '')))
def test_ruben(message):
    if message.text:
        return message.text=='!ruben' or message.text=='!RUBEN'
@bot.message_handler(func=test_ruben)
def send_ruben(message):
    if message.text=="!RUBEN":
        bot.send_photo(message.chat.id,photo='AgADBAADxKgxG6ME6VD7Swediqrc6wMXZhkABCaQ8K_aLGu4LeMCAAEC')
    else:
        bot.send_sticker(message.chat.id,data='BQADAgADeQMAAqdumAMqry1iBC9mnQI')
#@bot.message_handler(func=lambda message: message.reply_to_message)
@bot.message_handler(func=lambda message: False)
def cleverbot_reply(message):
    bot.reply_to(message,text=cb_ask(message.text.lower()))
def test_dot(message):
    if message.text:
        return message.from_user.id==130500414

@bot.message_handler(func=test_dot)
def sebas_dot(message):
    if not message.text[-1] is '.':
        reply=message.text + '.'
        bot.reply_to(message,reply)
@bot.message_handler(func=test_message)
def handle_text(message):
    word=search_coincidence(text_response,message.text.lower())
    if word:
        return bot.send_message(chat_id=message.chat.id, text=text_response[word],parse_mode="HTML")
    else:
        sticker = search_coincidence(sticker_response, message.text.lower())
        if sticker:
            bot.send_sticker(chat_id=message.chat.id,data=sticker_response[sticker])
        else:
            reply = search_coincidence(reply_response, message.text.lower())
            if reply:
                bot.reply_to(message, reply_response[reply],parse_mode="HTML")
            elif randint(0,100)==100:
                bot.send_message(chat_id=message.chat.id, text=cb_ask(message.text.lower()))


@bot.message_handler(content_types=['new_chat_member'])
def welcome(message):
    if message.from_user.id==0:
        bot.send_message(message.chat.id,"HUE HUE")
        bot.kick_chat_member(message.chat.id,59123141)
    elif message.new_chat_member.username:
        bot.send_message(message.chat.id, 'Hombre {0}, cuanto tiempo desde tu ultima expulsion'.format(message.new_chat_member.username))

    else:
        bot.send_message(message.chat.id, 'No se quien eres pero ya te estas poniendo un username')

