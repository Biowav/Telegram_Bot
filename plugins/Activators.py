from utils import *
import listener
father_id=87664746
@bot.message_handler(func=lambda message: False)
def nothing(message):
    pass

def db_update_on(message):
    if message.text:
        if message.from_user.id == father_id:
            return message.text == '!activate db updates'

def db_update_off(message):
    if message.text:
        if message.from_user.id == father_id:
            return message.text == '!deactivate db updates'

def check_db_status(message):
    if message.text:
        if message.from_user.id == father_id:
            return message.text == '!db status'

@bot.message_handler(func=check_db_status)
def db_status(message):
    if listener.update_ok:
        bot.send_message(chat_id=message.chat.id,text='Activado.')
    else:
        bot.send_message(chat_id=message.chat.id, text='Desactivado.')

@bot.message_handler(func=db_update_on)
def activate_updates(message):
    listener.update_ok=True


@bot.message_handler(func=db_update_off)
def deactivate_updates(message):
    listener.update_ok = False

@bot.message_handler(commands=['kclose'])
def close_keyboard(message):
    bot.send_message(chat_id=message.chat.id, text='Cerrando...',
                     reply_markup=types.ReplyKeyboardRemove(selective=False))

