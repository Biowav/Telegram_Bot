from utils import *
import random

def test_video(message):
    if message.text:
        return message.text[:6]=='!video'

videos={'islamic centrifugator':'https://vimeo.com/156988407',
        'soy programador':'https://www.youtube.com/watch?v=OgIRAjnnJzI'}
        #'karen':'https://www.youtube.com/watch?v=HrkrVPmnzbA'}


@bot.message_handler(func=test_video)
def send_music(message):
    video=message.text[7:]
    if video in videos:
        text =videos[video]
    elif video== 'list':
        text = '\n\n'.join(['%s: %s' % (k, v) for k, v in videos.items()])
    elif video == '':
        rand = random.choice(list(videos.keys()))
        text = videos[rand]
    else:
        text = 'no encuentro el video shur'
    bot.send_message(message.chat.id,text)
