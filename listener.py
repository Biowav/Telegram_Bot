import utils
from utils import *
import time
import datetime

last_listen = ''
update_ok = True


def check_user_db(message):
    aux_db = dbhelper.DBHelper()
    if not aux_db.get_user_by_id(message[-1].from_user.id):
        aux_db.add_user(message[-1].from_user.id, message[-1].from_user.first_name,
                        message[-1].from_user.last_name, message[-1].from_user.username)


def check_db_update(message):
    aux_db = dbhelper.DBHelper()
    aux_db.update(message[-1].from_user.id, message[-1].from_user.first_name,
                  message[-1].from_user.last_name, message[-1].from_user.username)


def check_username(message):
    aux_db = dbhelper.DBHelper()
    aux_db.check_username(message[-1].from_user.id, message[-1].from_user.username)


def show_poles(username, message):
    aux_db = dbhelper.DBHelper()
    poles = aux_db.show_poles(username)

    if poles:
        pole_text = "Las Poles de @" + username + ":\n"
        i = 0
        for pole in poles:
            i = i + 1
            pole_text += str(i) + '. ' + pole[3] + '  -  ' + pole[4] + "\n"
    else:
        pole_text = 'No encuentro las Poles'
    bot.send_message(message.chat.id, pole_text)
    pass


def show_inforpoles(username, message):
    aux_db = dbhelper.DBHelper()
    poles = aux_db.show_inforpoles(username)

    if poles:
        pole_text = "Las Poles de @" + username + ":\n"
        i = 0
        for pole in poles:
            i = i + 1
            pole_text += str(i) + '. ' + pole[3] + '  -  ' + pole[4] + "\n"
    else:
        pole_text = 'No encuentro las Poles'
    bot.send_message(message.chat.id, pole_text)
    pass


def listener(message):
    global last_listen
    last_listen = message[-1]
    if check_pole(last_listen):
        pole(last_listen)
    if check_inforpole(last_listen):
        inforpole(last_listen)
    if last_listen.text:
        if last_listen.text[:6] == "!poles":
            show_poles(last_listen.text[8:], last_listen)
        if last_listen.text[:7] == "!ipoles":
            show_inforpoles(last_listen.text[9:], last_listen)
    check_user_db(message)
    check_username(message)
    if update_ok:
        check_db_update(message)


def check_pole(message):
    db = dbhelper.DBHelper()
    if message.text:
        return int(time.strftime("%d", time.localtime())) != db.get_pole_day()[0][0] and message.chat.id == -195568193


def check_inforpole(message):
    db = dbhelper.DBHelper()
    if message.text:
        return int(time.strftime("%d", time.localtime())) != db.get_inforpole_day()[0][
            0] and message.chat.id == -219419208


def pole(message):
    db = dbhelper.DBHelper()
    pole_message = message.text
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db.add_pole(message.from_user.id, message.from_user.username, pole_message, date)
    i = 0
    if message.from_user.username:
        pole_response = "*La pole de hoy    " + datetime.datetime.now().strftime(
            "%Y-%m-%d") + "*\n" + message.from_user.username + " con " + '_"' + pole_message + '"_' + " a las " + datetime.datetime.now().strftime(
            "%H:%M:%S")
    else:
        pole_response = "*La pole de hoy    " + datetime.datetime.now().strftime(
            "%Y-%m-%d") + "*\n" + "Anónimo" + " con " + '_"' + pole_message + '"_' + " a las " + datetime.datetime.now().strftime(
            "%H:%M:%S")
    for i in range(0, 5):
        bot.send_message(chat_id=message.chat.id, text=pole_response, parse_mode="Markdown")


def inforpole(message):
    global poleman_id
    db = dbhelper.DBHelper()
    pole_message = message.text
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db.add_inforpole(message.from_user.id, message.from_user.username, pole_message, date)
    i = 0
    if message.from_user.username:
        pole_response = "<b>La pole de hoy    " + datetime.datetime.now().strftime(
            "%Y-%m-%d") + "</b>\n" + message.from_user.username + " con " + '<i>"' + pole_message + '"</i>' + " a las " + datetime.datetime.now().strftime(
            "%H:%M:%S")
    else:
        pole_response = "<b>La pole de hoy    " + datetime.datetime.now().strftime(
            "%Y-%m-%d") + "</b>\n" + "Anónimo" + " con " + '_"' + pole_message + '"_' + " a las " + datetime.datetime.now().strftime(
            "%H:%M:%S")
    for i in range(0, 5):
        bot.send_message(chat_id=message.chat.id, text=pole_response, parse_mode="HTML")
    bot.send_message(message.chat.id,
                     'Enhorabuena @' + message.from_user.username + ' durante 24h eres <strong>Poleman</strong>, '
                                                                    'tienes derecho a utilizar el comando <i>!kill {username}</i> para echar'
                                                                    ' gente del grupo <b>DIRECTAMENTE</b>. Utilizalo con prudencia.',
                     parse_mode='HTML')
    poleman_id=message.from_user.id
