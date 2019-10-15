import telebot
import dbhelper
import requests
import importdir
import time
from telebot import types
from random import randint

TOKEN = '303730127:AAGSPZ0QyD6Vub1AyKMb5xT-pxYb2-klnWM'
#TOKEN = '321563649:AAFGi70b42XFwn2nfNn6bv8xEK_oczsDG98'
bot = telebot.TeleBot(TOKEN)
db = dbhelper.DBHelper()
poleman_id=db.get_poleman_id()[0][0]
father_id=87664746
def get_poleman_id():
    db = dbhelper.DBHelper()
    id=db.get_poleman_id()[0][0]
    return id

first_time = True
clever_turn=2
def cb_ask(text):
    global clever_turn
    if clever_turn==2:
        response = requests.get(url='http://www.cleverbot.com/getreply',
                         params={'key': '727fc0797624c44ffceb17237e4b9fac', 'input': text}).json()
        clever_turn=1
    elif clever_turn==1:
        response = requests.get(url='http://www.cleverbot.com/getreply',
                                params={'key': '11181d7e6059713dfb603dab0b50e8a2', 'input': text}).json()
        clever_turn=0
    else:
        response = requests.get(url='http://www.cleverbot.com/getreply',
                                params={'key': '38e2bf642572b5569398a44372f3ceac', 'input': text}).json()
        clever_turn = 2
    return response['clever_output']
    #return 'No response'
def check_user(message):
    aux_db = dbhelper.DBHelper()
    if not aux_db.get_user_by_id(message[-1].from_user.id):
        aux_db.add_user(message[-1].from_user.id, message[-1].from_user.first_name,
                        message[-1].from_user.last_name, message[-1].from_user.username)


db_list={}

help_message='''/ruleta - ruleta rusa \n
!ruleta {username} - lanzas una ruleta para  {username} (cuidado) \n
/rpsls - piedra papel tijera lagarto spock (/rpsls rules para ver las reglas) \n
!monumento {monumento} - hay ciertas cosas en la vida que no debemos olvidar
monumentos: OW, stackoverflow y reverte\n
!edu - Frases del gran Eduardo Múgica\n
!music {nombre} - Envía una canción de la lista(!music list para ver la lista)\n
!b {libro}{versiculos} - Las palabras de nuestro señor\n
/tex {formula} - Envía una fotografía de la formula en formato LaTeX\n
!rng - Adivinar el número que piensa gauss (0-1000)\n
generar insultos - gauss insulta a {x}\n
Todas las noches a las 00:00 te podras marcar la pole del día\n
Si quieres dirigirte a gauss menciona su nombre o respondele, si le apetece te contestará'''

sticker_response={'pepe':'BQADBAADjAADlFkkCEoRGmKMm4FfAg',
                  'ANDER':'CAADBAADfQADO7egAAHPSeU0g4VXTgI',
                  'ander':'BQADBAADmQADO7egAAEjoRsPgXjtHwI',
                  'edu':'CAADBAADqQADO7egAAHQgKci-HcJ7QI',
                  'comer':'CAADBAAD9gADpkFVAAH86DRqgHIsfQI',
                  'roto2':'CAADBAADTwUAAo_pZgABpphj_80Kw4MC',
                  'report':'CAADBAAD9AQAAjZHEwABI2_9Ez7osXsC'}
text_response = {'mira macho': 'vete a la mierda',
                 'mujer': 'T_D_S P_T_S',
                 'increible':'https://twitter.com/LaurenJauregui/status/758683518872457216'
                 }
reply_response ={'hombre':'machete al machote',
                 'chin':'CHINA, EN CHINA HAY COMUNISMO',
                 'madur':'MADURO',
                 'juan':'Cuando esté lista avisar al profesor para que tome nota, e incluso sea testigo del funcionamiento de algún ping. Sin este paso <b>la práctica queda suspendida y no se podra recuperar</b>',
                 'whatsapp':'TODAVIA SE USA?',
                 'teresa':'Acoso'}
text_response.update(
    dict.fromkeys(['me voy', 'me largo', 'me abro', 'me piro', 'me retiro', 'me ire'], 'cierra al salir'))


edu_list = {
    'baños EEUU':'Lo mejor de EEUU son los baños, el nivel del agua es mas alto por lo que '
    'la mierda no se rompe con el impacto y puedes admirar tu obra. (Eduardo Múgica hablando con unas mujeres en la '
    'playa)',
    'socrates':'Que no tienes ni puta idea lo sabemos todos. (Eduardo Múgica en un acalorado debate con Sócrates)',
    'mujeres':'Si te sientes solo y estas cachondo, compra antidepresivos y cascate una buena paja, a la larga sale rentable'
    '(Eduardo Múgica en el discurso de entrega del premio nobel de la paz)',
    'simposio':'Una vez me hice una paja tan fuerte que con el calor generado por la fricción podria haber suministrado energía a toda la puta ciudad de Nueva York (Eduardo Múgica en un simposio sobre energías renovables)',
    'bautismo':'In nomine Patris et Filii et Spiritus Sancti. Amen. (Eduardo Múgica despues de cagar)',
    'mentira':'Hoy no se lía. (Eduardo Múgica mintiendose a si mismo)',
    'pregunta':'Preguntar es libre pero no se si me acordare de algo. (Eduardo Múgica mostrando su infinito conocimiento)',
    'pipa':'Tio, tengo la sensacion de que fumar de esa pipa me dio cancer desde la boca hasta los pulmones (Eduardo múgica en un domingo de resaca)',
    'giputxi':'¿Esta maquína no acepta dinero guiputxi o que? (Eduardo Múgica domando una máquina vending)',
    'paja': 'La pareja viene y va pero la paja siempre estará.'}

videos = {'la grange': 'https://www.youtube.com/watch?v=Vppbdf-qtGU',
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
          'girls just want to hace fun':'https://www.youtube.com/watch?v=PIb6AZdTr-A',
          'una vaina loca':'https://www.youtube.com/watch?v=IPBmNNWvUiQ',
          'irish pub':'https://www.youtube.com/watch?v=tDTQQWSmo8s',
          'the body of an American':'https://www.youtube.com/watch?v=q97IfBOIR5Q',
          'cuneta':'https://www.youtube.com/watch?v=PquTS397t-8',
          'echoes':'https://www.youtube.com/watch?v=53N99Nim6WE&t=692s',
          'forocoches':'https://www.youtube.com/watch?v=eeP896-Fq0c',
          'forofachas':'https://www.youtube.com/watch?v=QANCqO9nvzA',
          'johnny b. goode':'https://www.youtube.com/watch?v=ZFo8-JqzSCM',
          'you never can tell':'https://www.youtube.com/watch?v=RoDPPgWbfXY'
          }
