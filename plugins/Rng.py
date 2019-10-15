from utils import *
import listener


def test_rng(message):
    if message.text:
        return message.text[:4] == '!rng'


def game(message, secret_number, player_id, chat_id):
    if message.text.isdigit():
        if int(message.text) == secret_number:
            bot.send_message(chat_id, 'Has acertado')
            bot.kick_chat_member(chat_id, player_id)
        elif int(message.text) < secret_number:
            bot.send_message(chat_id, 'mas')
        else:
            bot.send_message(chat_id, 'menos')


def rng_game(player1_id, player2_id, chat_id):
    continue_game = True
    secret_number = randint(0, 1000)
    t_end = time.time() + 15
    player_turn = True
    while time.time() < t_end and continue_game:
        message = listener.last_listen
        if message.text:
            if message.from_user.id == player1_id and player_turn:
                game(message, secret_number, player2_id, chat_id)
                player_turn = not player_turn
                t_end = time.time() + 12
            if message.from_user.id == player2_id and not player_turn:
                if message.text.isdigit():
                    game(message, secret_number, player1_id, chat_id)
                    player_turn = not player_turn
                    t_end = time.time() + 12


@bot.message_handler(func=test_rng)
def rng(message):
    player1_id = message.from_user.id
    if message.text == '!rng':
        bot.send_message(message.chat.id, '¿HAY ALGUN VALIENTE QUE ACEPTE EL RETO?')
        play=True
        t_end=time.time()+8
        while time.time()<t_end and play:
            if listener.last_listen.text:
                if listener.last_listen.text.lower() == 'yo':
                    player2_id = listener.last_listen.from_user.id
                    if player1_id==player2_id:
                        bot.send_message(message.chat.id, 'No vayas de listo')
                        bot.kick_chat_member(message.chat.id,player1_id)
                        return
                    play=False
                    bot.send_message(message.chat.id, 'QUE COMIENCE EL JUEGO')
                    rng_game(player1_id, player2_id, message.chat.id)
