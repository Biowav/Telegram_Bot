from utils import *
import random

def test_music(message):
    if message.text:
        return message.text[:6]=='!music'



@bot.message_handler(func=test_music)
def send_music(message):
    song=message.text[7:]
    if song in videos:
        text =videos[song]
    elif song== 'list':
        text = '\n\n'.join(['%s_%s' % (k, v) for k, v in videos.items()])
    elif song == '':
        rand = random.choice(list(videos.keys()))
        text = videos[rand]
    else:
        text = 'no encuentro la cancion shur'
    bot.send_message(message.chat.id,text)
