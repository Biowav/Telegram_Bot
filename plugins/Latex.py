from utils import *
import subprocess

@bot.message_handler(commands=['tex'])
def tex(message):
    try:
        formula = message.text.replace('/tex', '').replace('+','{+}')
        subprocess.call('./pnglatex-master/pnglatex -f "' + formula + '" -d 1920 -o tex.png', shell=True)
        photo=open('tex.png', 'rb')
        bot.send_photo(chat_id=message.chat.id, photo=photo)
        subprocess.call('rm tex.png', shell=True)
    except Exception:
        bot.send_message(message.chat.id,'Escribelo bien ignorante hijo de puta.')