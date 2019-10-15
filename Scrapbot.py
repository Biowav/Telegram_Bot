from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import re
import time
import requests

token = '303730127:AAGSPZ0QyD6Vub1AyKMb5xT-pxYb2-klnWM'  # godelBot
in_message = ''
chat_id = -1
update_old = -1

lista_asignaturas = {'LCSI': '979', 'EDA': '3779', 'EBA': '1432', 'AC': '1703', 'MEI': '1751'}
lista_tutorias = {'LCSI': '979', 'AC': '1703'}


def get_updates():
    return requests.post(url='https://api.telegram.org/bot{0}/{1}'.format(token, 'getUpdates'),
                         data={'offset': '-1', 'timeout': 300}).json()


# devuelve la id del ultimo mensaje recibido
def get_chat(response):
    message = get_message(response)
    if 'chat' in message:
        return message['chat']['id']


# devuelve el ultimo mensaje recibido
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


# Envia un mensaje por telegram
def send_message(text):
    return requests.post(url='https://api.telegram.org/bot{0}/{1}'.format(token, 'sendMessage'),
                         data={'chat_id': chat_id, 'text': text}).json()


# envia un mensaje con las tutorias
def scrap_tutorias(url):
    text_tutorias = ''
    ff_binary = FirefoxBinary('/usr/bin/firefox')
    #browser = webdriver.Firefox(firefox_binary=ff_binary)
    browser=webdriver.PhantomJS()
    browser.get('https://egela1617.ehu.eus/login/index.php')

    username = browser.find_element_by_name('username')
    password = browser.find_element_by_name('password')

    username.send_keys('739176')
    password.send_keys('TralariTralara369258147')
    browser.find_element_by_xpath('''.//*[@id='loginbtn']''').click()
    #time.sleep(2)
    browser.get(url)
    source = browser.page_source
    titulos = '<span\ssize=\"[0-9]\"\sstyle=\"[a-z-]*:\s[a-z-]*;\">([^<]*)(<strong>)?([^<]*)(<\/strong>:)?' \
             '(<br\s\/>)?<\/span>'
    #titulos= '''((Lunes)|(Martes)|(Mi.rcoles)|(Jueves)|(Viernes)|(Asteartea)|(Asteazkena))(.*?)
    #([0-9]{,2}:[0-9]{2}\s?(-|(\sa\s))\s?[0-9]{2}:[0-9]{1,2})'''
    tutorias = re.findall(titulos, source)
    for x in tutorias:
        text_tutorias += x[0] + x[2] + "\n"
        #text_tutorias+=x[0]+" "+x[9]+"\n"
    send_message(text_tutorias)


# envia un mensaje con las calificaciones
def scrap_grades(url):
    text_grades = ''
    ff_binary = FirefoxBinary('/usr/bin/firefox')

    browser = webdriver.Firefox(firefox_binary=ff_binary)
    #browser=webdriver.PhantomJS()
    browser.get('https://egela1617.ehu.eus/login/index.php')

    username = browser.find_element_by_name('username')
    password = browser.find_element_by_name('password')

    username.send_keys('739176')
    password.send_keys('TralariTralara369258147')
    browser.find_element_by_xpath('''.//*[@id='loginbtn']''').click()
    time.sleep(2)
    browser.get(url)
    source = browser.page_source
    titulos = '(title=")((Tarea)|(Cuestionario)|(.tem manual)|(Assignment)|(Manual item))(" alt=")((Tarea)|(Cuestionario)|(.tem manual)|(Assignment)|(Manual item))" ?\/?>([^<]*)(<\/(a|(th))>)+'
    notas = '(<td\sheaders="cat)([0-9_]*\s(row)[0-9_]*)\s(grade" class=")(\s\sitem\sb1b\sitemcenter\s">)' \
            '((([0-9]+[.,][0-9]+)|-)?)<\/td>'
    lista_titulo = re.findall(titulos, source)
    lista_notas = re.findall(notas, source)
    i = 0
    while i < len(lista_notas):
        text_grades += lista_titulo[i][14] + ': ' + lista_notas[i][5] + '\n'
        i += 1
    send_message(text_grades)


def run():
    if in_message[:15] == '/calificaciones':
        if in_message[16:] in lista_asignaturas:
            url = 'https://egela1617.ehu.eus/grade/report/user/index.php?id={0}'.format(
                lista_asignaturas[in_message[16:]])
            scrap_grades(url)
        else:
            send_message('No encuentro la asignatura')
    elif in_message[:9] == '/tutorias':
        if in_message[10:] in lista_tutorias:
            url = 'https://egela1617.ehu.eus/course/view.php?id={0}'.format(lista_tutorias[in_message[10:]])
            scrap_tutorias(url)


while 1:
    time.sleep(0.3)
    updates = get_updates()

    chat_id = get_chat(updates)
    if updates['result']:
        update_id = updates['result'][-1]['update_id']
        in_message = get_text(updates)
        if update_id != update_old:
            run()
            update_old = update_id

pass
