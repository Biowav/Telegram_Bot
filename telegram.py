import requests
import datetime
import time
import random
from random import randint
igor_id = 11067132
lab_id = 10895793
edu_id = 90534552
chris_id = 215569741
isma_id = 127973022
father_id = 87664746
ander_id = 10532667
johan_id = 996206
rebeca_id = 90936008
danitxu_id = 173307110
elsa_id = 15448936

music = {'la grange':'https://www.youtube.com/watch?v=Vppbdf-qtGU',
         'child in time':'https://www.youtube.com/watch?v=PfAWReBmxEs',
         'smoke on the water': 'https://www.youtube.com/watch?v=zUwEIt9ez7M',
         'hallelujah': 'https://www.youtube.com/watch?v=YrLk4vdY28Q',
         'sound of silence': 'https://www.youtube.com/watch?v=4zLfCnGVeL4',
         'confortably numb': 'https://www.youtube.com/watch?v=_FrOQC-zEog',
         'wish you were here': 'https://www.youtube.com/watch?v=yvPr9YV7-Xw',
         'every breath you take': 'https://www.youtube.com/watch?v=OMOGaugKpzs',
         'have you ever seen the rain': 'https://www.youtube.com/watch?v=2oX2FSv4Rys',
         'father and son':'https://www.youtube.com/watch?v=VHjEtykqFmQ',
         'wild world': 'https://www.youtube.com/watch?v=0k6mQyu2GxM',
         'piece of my heart': 'https://www.youtube.com/watch?v=iJb7cBfrxbo',
         'stairway to heaven': 'https://www.youtube.com/watch?v=oW_7XBrDBAA',
         'bohemiam rhapsody': 'https://www.youtube.com/watch?v=fJ9rUzIMcZQ',
         'rising sun': 'https://www.youtube.com/watch?v=0sB3Fjw3Uvc',
         'chop suey': 'https://www.youtube.com/watch?v=CSvFpBOe8eY',
         'BYOB': 'https://www.youtube.com/watch?v=zUzd9KyIDrM',
         'cocaine': 'https://www.youtube.com/watch?v=pJyQpAiMXkg',
         'born to be wild': 'https://www.youtube.com/watch?v=rMbATaj7Il8',
         'paint it black': 'https://www.youtube.com/watch?v=InRDF_0lfHk',
         'all along the watchtower': 'https://www.youtube.com/watch?v=TLV4_xaYynY',
         'the end':'https://www.youtube.com/watch?v=JSUIQgEVDM4',
         'riders on the storm': 'https://www.youtube.com/watch?v=BLBV6ZwLKDU',
         'smells like teen spirit': 'https://www.youtube.com/watch?v=hTWKbfoikeg',
         "sweet child o'mine": 'https://www.youtube.com/watch?v=1w7OgIMMRc4',
         'take on me': 'https://www.youtube.com/watch?v=djV11Xbc914',
         'girls just want to hace fun':'https://www.youtube.com/watch?v=PIb6AZdTr-A'
         }

esto_que_es_id = 'BQADBAADiwADaqg5BYPvVKVNZHnFAg'
players = {'igor':11067132,'lab':10895793,'edu':90534552,'chris':215569741,'isma':127973022,'ander':10532667,'dani':87664746, 'johan':johan_id,'rebeca':90936008}
edu_list = [
    'Lo mejor de EEUU son los baños, el nivel del agua es mas alto por lo que '
    'la mierda no se rompe con el impacto y puedes admirar tu obra. (Eduardo Múgica hablando con unas mujeres en la '
    'playa)',
    'Que no tienes ni puta idea lo sabemos todos. (Eduardo Múgica en un acalorado debate con Sócrates)',
    'Si te sientes solo y estas cachondo, compra antidepresivos y cascate una buena paja, a la larga sale rentable'
    '(Eduardo Múgica en el discurso de entrega del premio nobel de la paz)',
    'Una vez me hice una paja tan fuerte que con el calor generado por la fricción podria haber suministrado energía a toda la puta ciudad de Nueva York (Eduardo Múgica en un simposio sobre energías renovables)',
    'In nomine Patris et Filii et Spiritus Sancti. Amen. (Eduardo Múgica despues de cagar)',
    'Hoy no se lía. (Eduardo Múgica mintiendose a si mismo)',
    'Preguntar es libre pero no se si me acordare de algo. (Eduardo Múgica mostrando su infinito conocimiento)',
    'Tio, tengo la sensacion de que fumar de esa pipa me dio cancer desde la boca hasta los pulmones (Eduardo múgica en un domingo de resaca)',
    '¿Esta maquína no acepta dinero guiputxi o que? (Eduardo Múgica domando una máquina vending)']

luis_list = ['Jodo.', 'Co', 'K cebao', 'No tiene sentido', 'Pero que no tiene ningun sentido, eh?', 'que????',
             'alguna vez has probado a mear en una botella?',
             'perse es una locución del latin que significa soy pedante']
chris_stickers = ['BQADBAAD9hMAAnrRWwYGHGHBfbTFHQI', 'BQADBAAD-BMAAnrRWwYKKPzuJvvgPQI']


class Telegram:
    def __init__(self):
        self.text = ''
        # self.token = '323987975:AAF0caZCBdoLh2lco3Bv21n12KcONh7MZ_k'
        self.token = '303730127:AAGSPZ0QyD6Vub1AyKMb5xT-pxYb2-klnWM'  # godelBot
        self.user = {'id': 0,
                     'first_name': ''}
        self.chat = {'id': 0,
                     'type': ''}
        self.message_id = -1

    # Devuelve informacion del token
    def get_me(self):
        return requests.post(url='https://api.telegram.org/bot{0}/{1}'.format(self.token, 'getMe')).json()

    def get_updates(self):
        return requests.post(url='https://api.telegram.org/bot{0}/{1}'.format(self.token, 'getUpdates'),
                             data={'offset': '-1', 'timeout': 300}).json()

    def get_meme(self):
        top='tralari'
        down='tralara'
        meme = requests.post(url='http://version1.api.memegenerator.net/Instance_Create',
                             data={'username':'test', 'password':'test','languageCode':'en','generadorID':45,
                                   'imageID':20} ).json()
        index = randint(0, 99)
        self.load_target(meme['data']['memes'][index]['url'], self.chat['id'])
        self.send_message()


    # guarda el id y el nombre de un usuario
    def get_user(self, response):
        message = get_message(response)
        if 'from' in message:
            self.user['id'] = message['from']['id']
            self.user['first_name'] = message['from']['first_name']
            return message['from']
            # guarda el id y el tipo de un chat

    def get_chat(self, response):
        message = get_message(response)
        if 'chat' in message:
            self.chat['id'] = message['chat']['id']
            self.chat['type'] = message['chat']['type']
            self.message_id = message['message_id']

    def set_time(self):
        self.text = datetime.datetime.now()
        self.send_message()

    # carga el id del chat y el texto en las variables
    def load_target(self, text, chat_id=0):
        if chat_id:
            self.chat['id'] = chat_id
        self.text = text

    def set_sentence_edu(self):
        index = randint(0, len(edu_list) - 1)
        self.load_target(edu_list[index], self.chat['id'])

    # devuelve una palabra de la lista de luis
    def set_sentence_luis(self):
        index = randint(0, len(edu_list) - 1)
        self.load_target(luis_list[index], self.chat['id'])


    # expulsa a un miembro del grupo
    def kick(self):
        requests.post(url='https://api.telegram.org/bot{0}/{1}'.format(self.token, 'kickChatMember'),
                      data={'chat_id': self.chat['id'], 'user_id': self.user['id']}).json()

    def kill(self,target):
        if self.user['id']==father_id:
            self.user['id']=players[target]
            self.kick()


    def kick_member(self):
        index = randint(0, 5)
        if (index == 5):
            self.text = 'Descansa en paz...'
            self.send_message()
            return self.kick()
        else:
            self.text = 'Te has librado'
            self.reply()

    def ruleta_igor(self):
        self.ruleta('igor', igor_id)

    def ruleta_lab(self):
        self.ruleta('lab', lab_id)

    def ruleta_edu(self):
        self.ruleta('edu', edu_id)

    def ruleta_chris(self):
        self.ruleta('chris', chris_id)

    def ruleta_danitxu(self):
        self.ruleta('danitxu', danitxu_id)

    def ruleta_isma(self):
        self.ruleta('isma', isma_id)

    def ruleta_ander(self):
        self.ruleta('ander', ander_id)

    def ruleta_johan(self):
        self.ruleta('johan', johan_id)

    def ruleta_rebeca(self):
        self.ruleta('rebeca', rebeca_id)
    def ruleta_elsa(self):
        self.ruleta('elsa',elsa_id)

    def ruleta_all(self):
        if self.user['id'] == father_id:
            self.ruleta_igor()
            self.ruleta_edu()
            self.ruleta_ander()
            self.ruleta_lab()
            self.ruleta_chris()
            self.ruleta_isma()
        else:
            self.text = 'Tu que haces'
            self.reply()
            self.kick_member()

    def ruleta(self, user, id):
        index = randint(0, 5)
        coin = randint(0, 2)
        if (coin <= 1) or self.user['id'] == father_id:
            alive = self.save_from_kick()
            if alive:
                if (index == 5):
                    self.text = 'Descansa en paz...'
                    self.send_message()

                    return requests.post(url='https://api.telegram.org/bot{0}/{1}'.format(self.token, 'kickChatMember'),
                                         data={'chat_id': self.chat['id'], 'user_id': id}).json()
                else:
                    self.text = 'Te has salvado ' + user
                    self.send_message()
        else:
            self.text = 'Ruleta para ti chaval'
            self.reply()
            self.kick_member()

    def save_from_kick(self):
        old_id = self.user['id']
        not_found = True
        t_end = time.time() + 3
        while time.time() < t_end and not_found:
            new_updates = self.get_updates()
            if 'sticker' in new_updates['result'][-1]['message'] and not_found:
                if new_updates['result'][-1]['message']['sticker']['file_id'] == 'BQADBAAD9AIAAp-t1gABo7IGGV6JAa8C':
                    not_found = False

                    self.text = 'CONTRAHECHIZO'
                    self.send_message()
                    self.user['id'] = old_id
                    self.kick()
            elif new_updates['result'][-1]['message']['text'].lower() == 'ch' and not_found:
                not_found = False
                self.text = 'Contrahechizo'
                self.send_message()
        return not_found

    def send_message(self):
        return requests.post(url='https://api.telegram.org/bot{0}/{1}'.format(self.token, 'sendMessage'),
                             data={'chat_id': self.chat['id'], 'text': self.text}).json()

    def send_audio(self):
        return requests.post(url='https://api.telegram.org/bot{0}/{1}'.format(self.token, 'sendVoice'),
                             data={'chat_id': self.chat['id'], 'voice': 'AwADBAAD5kkAAskcZAfcP-f9fGPtGgI'}).json()

    def send_music(self,song):
        if song in music:
            self.text=music[song]
        elif song=='list':
            self.text = '\n\n'.join(['%s_%s' % (k,v) for k,v in music.items()])
        elif song=='':
           rand = random.choice(list(music.keys()))
           self.text = music[rand]
        else:
            self.text = 'no encuentro la cancion shur'
        self.send_message()

    def rpsls(self):
        plays=['piedra', 'spock', 'papel','lagarto', 'tijera', 'r', 's','p','l','t']
        not_play=True
        self.text = 'Piedra papel tijera lagarto Spock \n \npiedra - r \npapel - p \ntijera - t \nlagarto - l \nspock - s'
        self.send_message()
        t_end=time.time()+5
        while time.time()<t_end and not_play:
            new_updates = self.get_updates()
            message = new_updates['result'][-1]['message']['text'].lower()
            if message in plays:
                not_play=False
                player_number = self.name_to_number(message)
                comp_number = random.randrange(0, 4)
                self.text=plays[comp_number]
                self.send_message()
                if (comp_number + 1) % 5 == player_number:
                    self.text = 'Has Ganado'
                elif (comp_number + 2) % 5 == player_number:
                    self.text = 'Has Ganado'
                elif comp_number == player_number:
                    self.text = 'Empate'
                else:
                    self.text = 'Has Perdido'
                self.send_message()
    def number_to_name(self,num):
        if num == 0:
            result = "piedra"
        elif num == 1:
            result = "spock"
        elif num == 2:
            result = "papel"
        elif num == 3:
            result = "lagarto"
        elif num == 4:
            result = "tijera"
        return result

    def name_to_number(self,name):
        if name == "piedra" or name == "r":
            result = 0
        elif name == "spock" or name == "s":
            result = 1
        elif name == "papel" or name == "p":
            result = 2
        elif name == "lagarto" or name == "l":
            result = 3
        elif name == "tijera" or name == "t":
            result = 4

        return result
    def rpsls_human(self,user):
        player1_id = self.user['id']
        player2_id = players[user]
        if player1_id == player2_id:
            self.text = 'a la puta calle'
            self.send_message()
            self.user['id'] = player2_id
            self.kick()
        else:
            t_end=time.time()+8
            self.text = 'aceptas el reto?'
            self.send_message()
            while time.time()<t_end:




                new_updates=self.get_updates()
                message = new_updates['result'][-1]['message']['text'].lower()
                id = new_updates['result'][-1]['message']['from']['id']
                if message=='go' and id==player2_id:
                    self.text = 'Que empiece el juego.'
                    self.send_message()
                    number=randint(0,1000)
                    player1_turn=True
                    player2_turn=False
                    play = True
                    t_end2 = time.time() + 12
                    while time.time() < t_end2 and play:
                        new_updates = self.get_updates()
                        if (new_updates['result'][-1]['message']['from']['id']==player1_id and player1_turn):
                            play1 = new_updates['result'][-1]['message']['text']
                            if play1.isdigit():
                                if int(play1)==number:
                                    self.text='Has acertado'
                                    self.send_message()
                                    self.user['id']=player2_id
                                    self.kick()
                                    play=False
                                elif int(play1)<number:
                                    self.text='mas'
                                    self.send_message()
                                else:
                                    self.text = 'menos'
                                    self.send_message()
                                t_end2=time.time()+12
                                player1_turn = False
                                player2_turn = True
                        if (new_updates['result'][-1]['message']['from']['id']==player2_id and player2_turn):
                            play1 =new_updates['result'][-1]['message']['text']
                            if play1.isdigit():
                                if int(play1)==number:
                                    self.text='Has acertado'
                                    self.send_message()
                                    play=False
                                    self.user['id']=player1_id
                                    self.kick()
                                elif int(play1)<number:
                                    self.text='mas'
                                    self.send_message()
                                else:
                                    self.text = 'menos'
                                    self.send_message()
                                t_end2 = time.time() + 12
                                player1_turn = True
                                player2_turn = False


    def rpsls_rules(self):
        self.text = 'Tijeras cortan papel, papel envuelve piedra,  piedra aplasta lagarto, lagarto envenena a Spock, ' \
                    'Spock rompe tijeras, tijeras decapitan lagarto, lagarto come papel, papel desautoriza a Spock, ' \
                    'Spock desintegra piedra y como siempre piedra aplasta tijeras'
        self.send_message()

    def stackoverflow_link(self):
        self.text = 'http://stackoverflow.com/questions/15445285/how-can-i-connect-to-a-tor-hidden-service-using-curl-in-php'
        self.send_message()
    def reply(self):
        return requests.post(url='https://api.telegram.org/bot{0}/{1}'.format(self.token, 'sendMessage'),
                             data={'chat_id': self.chat['id'], 'text': self.text,
                                   'reply_to_message_id': self.message_id}).json()

    def reportar(self):
        return requests.post(url='https://api.telegram.org/bot{0}/{1}'.format(self.token, 'sendSticker'),
                             data={'chat_id': self.chat['id'], 'sticker': 'BQADBAADUgUAAo_pZgAB4JFKo-rKQFMC'}).json()

    def contrahechizo(self):
        return requests.post(url='https://api.telegram.org/bot{0}/{1}'.format(self.token, 'sendSticker'),
                             data={'chat_id': self.chat['id'], 'sticker': 'BQADBAAD9AIAAp-t1gABo7IGGV6JAa8C'}).json()

    def ander_sticker(self):
        return requests.post(url='https://api.telegram.org/bot{0}/{1}'.format(self.token, 'sendSticker'),
                             data={'chat_id': self.chat['id'], 'sticker': 'BQADBAADmQADO7egAAEjoRsPgXjtHwI'}).json()

    def comeatme(self):
        return requests.post(url='https://api.telegram.org/bot{0}/{1}'.format(self.token, 'sendPhoto'),
                             data={'chat_id': self.chat['id'], 'photo': 'AgADBAADV6kxG2qoOQVnsqolw9N6_5xQaRkABKQkZAxpI4BIl-MCAAEC'}).json()

    def chris_sticker(self):
        index = randint(0, len(chris_stickers) - 1)
        return requests.post(url='https://api.telegram.org/bot{0}/{1}'.format(self.token, 'sendSticker'),
                             data={'chat_id': self.chat['id'], 'sticker': chris_stickers[index]}).json()

    def monumento_chris(self):
        self.text = 'menuda mieda el OW le van a dar bien por el culo. Solo he ganado una ridiculo me mete con gente de nivel' \
                ' 600 y pone que son partidas con gente de tu misma habilidad un tio de 600 horas la misma habilidad que yo en 1h' \
                ' que le den por el culo no me vuelvo a comprar nada multijugador en mi vida que ascazo hostia puta. No tiene nada ' \
                ' es meterte a un online que no quiere que te guste el juego amargandote contra puta gente que te saca 70 niveles minimo.' \
                ' lo dejare ahi para que me recuerde mi tremenda estupidez. Cada vez que lo vea me acordare de igor y de su santa madre.'


    def pepefront_sticker(self):
        return requests.post(url='https://api.telegram.org/bot{0}/{1}'.format(self.token, 'sendSticker'),
                             data={'chat_id': self.chat['id'], 'sticker': 'BQADBAADjAADlFkkCEoRGmKMm4FfAg'}).json()

    def send_sticker(self):
        return requests.post(url='https://api.telegram.org/bot{0}/{1}'.format(self.token, 'sendSticker'),
                             data={'chat_id': self.chat['id'], 'sticker': self.text}).json()
    def cuenta_atras(self):
        no_stop=True
        t = time.time()
        tiempo=10
        while no_stop:
            if time.time()>t:
                self.text = tiempo
                self.send_message()
                tiempo=tiempo-1
                t=time.time()+1
            if tiempo==0:
                no_stop=False
        time.sleep(1)
        self.text = 'GO'
        self.send_message()
# devuelve el mensaje
def get_message(response):
    if response['ok'] and response['result']:
        result = response['result']
        if 'message' in result[-1]:
            return result[-1]['message']


# devuelve el texto del mensaje
def get_text(response):
    if response['ok']:
        result = response['result']

        if 'message' in result[-1]:
            message = result[-1]['message']
            if 'text' in message:
                return message['text']
