import telegram as tg
import re
from random import randint
from cleverbot import Cleverbot

telegram = tg.Telegram()
cleverbot = Cleverbot()
key_words2={}
def ask_cleverbot(in_message):
    telegram.load_target(cleverbot.ask(in_message.lower().replace('gauss', ''))
                         , telegram.chat['id'])
    telegram.send_message()
def send_message(in_message):
    telegram.load_target(in_message
                         , telegram.chat['id'])
    telegram.send_message()
def reply_message(in_message):
    telegram.load_target(key_words[in_message]
                         , telegram.chat['id'])
    telegram.reply()
def send_sticker(sticker_id):
    telegram.load_target(sticker_id,telegram.chat['id'])
    telegram.send_sticker()

in_message = ''
response=''
once_a_day = True
players = {'igor':11067132,'lab':10895793,'edu':90534552,'chris':215569741,'isma':127973022,'ander':10532667,'dani':87664746,'johan':996206}

words_list = ['hola', 'que', 'que te pica', 'cabron', 'mira macho', 'que te calles', 'puto igor', 'a tomar por culo',
              'jeje',
              'de tiro largo y de forma de campaaaanaaa', 'xddddddddddddddddddddd']
selios_list = ['buaaah chaval que guapo', 'miiiiira chavaaaaal', 'el arbolito chaval',
               'he comprao un arbol chaval', 'A GUA CHUBiDuBi NaAanaN', 'suputamadre chaval', 'que guaaapo chaval',
               'Tranquilo', 'las barracudas chaval', 'buah chaval me ha parado la policia']
key_words = {'mira macho': 'vete a la mierda',
              'me ayudas?': 'a fregar',
              'se van a pelear': 'mi polla y tu paladar',
              'esta cachas': 'el que te da por el culo cuando te agachas',
              'mujer': 'T_D_S P_T_S'}
sticker_words = {'reportado':'BQADBAADUgUAAo_pZgAB4JFKo-rKQFMC'}

games = {'/rpsls':'rpsls',
         '/rng vs': 'rpsls_rules'}
commands = {'/time': 'set_time',
            '/rpsls':'rpsls',
            '/rpsls rules':'rpsls_rules',
            '/rng vs':'rpsls_human',
            '/ruleta': 'kick_member',
            '/contrahechizo': 'contrahechizo',
            '/time@GodelBot': 'set_time',
            '/ruleta@GodelBot': 'kick_member',
            '/reportar@GodelBot': 'reportar',
            '/contrahechizo@GodelBot': 'contrahechizo',
            '/mm' : 'get_meme',
            '/ruleta igor': 'ruleta_igor',
            '/ruleta lab': 'ruleta_lab',
            '/ruleta edu': 'ruleta_edu',
            '/ruleta chris': 'ruleta_chris',
            '/ruleta isma': 'ruleta_isma',
            '/ruleta ander': 'ruleta_ander',
            '/ruleta johan': 'ruleta_johan',
            '/ruleta all': 'ruleta_all',
            '/cuenta': 'cuenta_atras'
            }

frases = {'!edu': 'set_sentence_edu',
          '!monumento stackoverflow': 'stackoverflow_link',
          '!luis': 'set_sentence_luis'
          }


update_old = -1
in_message=''
in_message_copy=''
response=''

def search(list):
    for word in list:
        if word in in_message:
            global response
            response = word
            return True
def run(user_id):
    if 'gauss' in in_message:
        ask_cleverbot(in_message)
    elif (search(key_words)):
        send_message(key_words[response])
    elif (search(sticker_words)):
        send_sticker(sticker_words[response])
    elif in_message in commands:
        getattr(telegram, commands[in_message])(in_message)
    elif in_message in frases:
        getattr(telegram, frases[in_message])()
        telegram.send_message()



while 1:
    updates = telegram.get_updates()

    telegram.get_chat(updates)
    user_id=telegram.get_user(updates)
    if updates['result']:
        update_id = updates['result'][-1]['update_id']
        in_message = tg.get_text(updates)
        if update_id != update_old:
            run(user_id)
            update_old = update_id

pass
