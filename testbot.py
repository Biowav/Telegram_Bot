import telegram as tg
import time
from random import randint
from cleverbot import Cleverbot
import requests

once_a_day = True
players = {'igor':11067132,'lab':10895793,'edu':90534552,'chris':215569741,'isma':127973022,'ander':10532667,'dani':87664746,'johan':996206,'rebeca':90936008}

words_list = ['hola', 'que', 'que te pica', 'cabron', 'mira macho', 'que te calles', 'puto igor', 'a tomar por culo',
              'jeje',
              'de tiro largo y de forma de campaaaanaaa', 'xddddddddddddddddddddd']
selios_list = ['buaaah chaval que guapo', 'miiiiira chavaaaaal', 'el arbolito chaval',
               'he comprao un arbol chaval', 'A GUA CHUBiDuBi NaAanaN', 'suputamadre chaval', 'que guaaapo chaval',
               'Tranquilo', 'las barracudas chaval', 'buah chaval me ha parado la policia']
key_words = {'gauss'}
key_words2 = {'mira macho': 'vete a la mierda',
              'me ayudas?': 'a fregar',
              'se van a pelear': 'mi polla y tu paladar',
              'esta cachas': 'el que te da por el culo cuando te agachas',
              '!españa':'https://www.youtube.com/watch?v=QUMMDrMkhYA'}
sitcker_words = {'reportado'}
commands = {'/time': 'set_time',
            '/rpsls':'rpsls',
            '/rpsls rules':'rpsls_rules',
            '/rng vs':'rpsls_human',
            '/ruleta': 'kick_member',
            '/reportar': 'reportar',
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
            '/ruleta rebeca': 'ruleta_rebeca',
            '/ruleta danitxu': 'ruleta_danitxu',
            '/ruleta elsa':'ruleta_elsa',
            '/ruleta all': 'ruleta_all',
            'gauss cuenta atras': 'cuenta_atras',
            '/kill':'kill'
            }

frases = {'!edu': 'set_sentence_edu',
          '!monumento stackoverflow': 'stackoverflow_link',
          '!monumento OW': 'monumento_chris',
          '!españa'
          '!luis': 'set_sentence_luis',
          '!music': 'send_music'
          }

audio = {'la grange':'send_music'}
telegram = tg.Telegram()
cleverbot = Cleverbot('Gauss')

update_old = -1
in_message=''
in_message_copy=''
def run(user_id):
    in_message_copy = ''
    if isinstance(in_message, str):
        in_message_copy=in_message
    if (in_message not in commands) and (in_message not in frases) and (in_message_copy[:7]!='/rng vs') and (in_message_copy[:6]!='!music') and (in_message_copy[:5]!='/kill'):
        if 'reply_to_message' in updates['result'][-1]['message']:
            telegram.load_target(cleverbot.ask(in_message), telegram.chat['id'])
            telegram.reply()
        else:
            if telegram.user['id'] == 0000:  # father_id
                telegram.text = 'Mensaje archivado en el libro: Grandes frases de Eduardo Múgica, rey de reyes. Gracias por compartir tu sabiduria con nosotros.'
                index = randint(0, len(telegram.edu_list) - 1)
                telegram.send_message()
                telegram.load_target(telegram.edu_list[index], telegram.chat['id'])
                telegram.send_message()
            else:
                if in_message:
                    if  ('gauss' in in_message.lower()): # compara si hay algun elemento comun en las listas
                        telegram.load_target(cleverbot.ask(in_message.lower().replace('gauss', ''))
                                             , telegram.chat['id'])
                        telegram.send_message()
                    else:
                        if ('mujer' in in_message.lower()):
                            telegram.load_target('T_D_S P_T_S'
                                                 , telegram.chat['id'])
                            telegram.send_message()

                        if('!mensaje' in in_message.lower()):
                            #telegram.load_target(in_message[9:]
                            #                     , -195568193)
                            telegram.load_target(in_message[9:]
                                                 , 12661796)
                            telegram.send_message()

                        elif ('ander' in in_message.lower()):
                            telegram.ander_sticker()

                        elif('come at me' in in_message.lower()):
                            telegram.comeatme()

                        elif ('pepe' in in_message.lower()):
                            telegram.pepefront_sticker()

                        elif ('esto que es' in in_message.lower() or 'que es esto' in in_message.lower()):
                            telegram.send_audio()

                        elif ('chris' in in_message.lower()) or ('cris' in in_message.lower()):
                            telegram.chris_sticker()

                        elif ('me voy' in in_message.lower()) or ('me largo' in in_message.lower()) or ('me abro' in in_message.lower()):
                            telegram.load_target('Cierra al salir'
                                                 , telegram.chat['id'])
                            telegram.send_message()

                        elif ('madur' in in_message.lower()):
                            telegram.load_target('MADURO'
                                                 , telegram.chat['id'])
                            telegram.reply()

                        elif ('chin' in in_message.lower()):
                            telegram.load_target('CHINA, EN CHINA HAY COMUNISMO'
                                                 , telegram.chat['id'])
                            telegram.reply()
                        elif ('hombre' in in_message.lower()):
                            telegram.load_target('machete al machote'
                                                 , telegram.chat['id'])
                            telegram.reply()
                        elif ('chaval' in in_message.lower() or 'selios' in in_message.lower() or 'tranquilo' in in_message.lower()):
                            index = randint(0, len(selios_list) - 1)
                            telegram.load_target(selios_list[index], telegram.chat['id'])
                            telegram.send_message()
                        elif (randint(0,25)==10 and in_message):
                            telegram.load_target(cleverbot.ask(in_message.lower())
                                                 , telegram.chat['id'])
                            telegram.send_message()


                        elif in_message in key_words2:
                            telegram.load_target(key_words2[in_message]
                                                 , telegram.chat['id'])
                            telegram.send_message()

    else:
        if (in_message[:6] == '!music'):
            getattr(telegram, frases[in_message[:6]])(in_message[7:])
        elif (in_message in frases):

            getattr(telegram, frases[in_message])()
            telegram.send_message()

        elif(in_message[:7] == '/rng vs'):
            if(in_message[8:] in players):
                getattr(telegram, commands[in_message[:7]])(in_message[8:])
        elif(in_message[:5] == '/kill'):
            if (in_message[6:] in players):
                getattr(telegram, commands[in_message[:5]])(in_message[6:])
        else:
            getattr(telegram, commands[in_message])()


while 1:

    time.sleep(0.3)
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
