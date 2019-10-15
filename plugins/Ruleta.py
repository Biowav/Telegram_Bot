from utils import *
import listener

i = 6

frases_ruleta = ['Todos sabemos lo que viene ahora, ¿No es así?', 'Se un hombre y acaba con esto de una vez.']


def ruleta(message, user_id):
    if (randint(0, 5) == 5):
        text = 'La suerte no esta de tu parte amig@. <b>Descansa en paz...</b>'
        bot.send_message(chat_id=message.chat.id, text=text, parse_mode="HTML")

        bot.kick_chat_member(message.chat.id, user_id)
    else:
        text = 'El tiro ha fallado, <b>te has salvado</b> ' + message.text[9:]
        bot.send_message(chat_id=message.chat.id, text=text, parse_mode="HTML")


def ruleta_rusa(message, user_id):
    global i
    if (randint(1, i) == 1):
        i = 6
        text = 'La suerte no esta de tu parte amig@. <b>Descansa en paz...</b>'
        bot.send_message(chat_id=message.chat.id, text=text, parse_mode="HTML")
        bot.kick_chat_member(message.chat.id, user_id)

    else:
        i = i - 1
        if i == 1:
            text = 'El tiro ha fallado, <b>te has salvado</b> ' + message.text[9:] + '. Queda ' + str(i) + ' bala. ' + \
                   frases_ruleta[randint(0, len(frases_ruleta) - 1)]
        else:
            text = 'El tiro ha fallado, <b>te has salvado</b> ' + message.text[9:] + '. Quedan ' + str(i) + ' balas.'

        bot.send_message(chat_id=message.chat.id, text=text, parse_mode="HTML")


@bot.message_handler(commands=['ruleta'])
def ruleta_self(message):
    ruleta_rusa(message, message.from_user.id)


def check_message(message):
    if message.text:
        return message.text[:8] == '!ruleta '


def check_message_antiruleta(message):
    if message.text:
        return message.text[:8] == '!ruIeta '


# Decide si se anula la ruleta
def save_from_kick(user_id, chat_id):
    t_end = time.time() + 3
    while time.time() < t_end:
        response = listener.last_listen
        if response.sticker:
            if response.sticker.file_id == 'CAADBAAD9AIAAp-t1gABo7IGGV6JAa8C':
                bot.send_message(chat_id=chat_id, text='CONTRAHECHIZO')
                bot.kick_chat_member(chat_id, user_id)
                return False
        elif response.text == 'ch' or response.text == 'Ch':
            bot.send_message(chat_id=chat_id, text='contrahechizo')
            return False
    return True


def kill_antiruleta(chat_id):
    t_end = time.time() + 3
    while time.time() < t_end:
        response = listener.last_listen
        if response.sticker:
            if response.sticker.file_id == 'CAADBAAD9AIAAp-t1gABo7IGGV6JAa8C':
                bot.send_message(chat_id=chat_id, text='ANTIRULETA')
                bot.kick_chat_member(chat_id, response.from_user.id)
                return False
    return True


@bot.message_handler(func=check_message)
def ruleta_for(message):
    db = dbhelper.DBHelper()
    for_user = db.get_user_by_username(message.text[9:])
    if for_user:
        for_user_id = for_user[0][1]
        coin = randint(0, 1)
        if (coin <= 1):
            death = save_from_kick(message.from_user.id, message.chat.id)
            if death:
                ruleta(message, for_user_id)
        else:
            bot.send_message(chat_id=message.chat.id, text='Ruleta para ti chaval')
    else:
        bot.send_message(chat_id=message.chat.id, text='No conozco a ningun ' + message.text[8:])


@bot.message_handler(func=check_message_antiruleta)
def antiruleta(message):
    db = dbhelper.DBHelper()
    for_user = db.get_user_by_username(message.text[9:])
    if for_user:
        death = kill_antiruleta(message.chat.id)
        if death:
            ruleta(message, message.from_user.id)
