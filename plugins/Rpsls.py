from utils import *
import listener

count = 1

def rpsls_rules(message):
    if message.text:
        return message.text=='/rpsls rules'

def has_username(message):
    if message.from_user:
        return not (message.from_user.username)


@bot.message_handler(func=rpsls_rules)
def rpsls_rules_message(message):
    text='Tijeras cortan papel, papel envuelve piedra,  piedra aplasta lagarto, lagarto envenena a Spock, ' \
                    'Spock rompe tijeras, tijeras decapitan lagarto, lagarto come papel, papel desautoriza a Spock, ' \
                    'Spock desintegra piedra y como siempre piedra aplasta tijeras.'
    bot.send_message(message.chat.id,text=text)


@bot.message_handler(commands=['rpsls'])
def rpsls(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, selective=True)
    markup.add('Piedra', 'Spock', 'Papel', 'Lagarto', 'Tijera')
    plays = ['Piedra', 'Spock', 'Papel', 'Lagarto', 'Tijera', 'r', 's', 'p', 'l', 't']
    not_play = True
    text = '@' + message.from_user.username + ' Piedra papel tijera lagarto Spock \n \nPiedra - r \nPapel - p \nTijera - t \nLagarto - l \nSpock - s'
    bot.send_message(chat_id=message.chat.id, text=text, reply_markup=markup)
    t_end = time.time() + 5
    while time.time() < t_end and not_play:
        response = listener.last_listen.text
        if response in plays:
            not_play = False
            player_number = name_to_number(response)
            comp_number = randint(0, 4)
            text = plays[comp_number]
            bot.send_message(chat_id=message.chat.id, text=text)
            if (comp_number + 1) % 5 == player_number:
                text = 'Has Ganado'
            elif (comp_number + 2) % 5 == player_number:
                text = 'Has Ganado'
            elif comp_number == player_number:
                text = 'Empate'
            else:
                text = 'Has Perdido'

            bot.send_message(chat_id=message.chat.id, text=text,
                             reply_markup=types.ReplyKeyboardRemove(selective=False))


def number_to_name(num):
    if num == 0:
        result = "Piedra"
    elif num == 1:
        result = "Spock"
    elif num == 2:
        result = "Papel"
    elif num == 3:
        result = "Lagarto"
    elif num == 4:
        result = "Tijera"
    return result


def name_to_number(name):
    if name == "Piedra" or name == "r":
        result = 0
    elif name == "Spock" or name == "s":
        result = 1
    elif name == "Papel" or name == "p":
        result = 2
    elif name == "Lagarto" or name == "l":
        result = 3
    elif name == "Tijera" or name == "t":
        result = 4

    return result
