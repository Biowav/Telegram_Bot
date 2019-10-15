from utils import *

selios_list = ['buaaah chaval que guapo', 'miiiiira chavaaaaal', 'el arbolito chaval',
               'he comprao un arbol chaval', 'A GUA CHUBiDuBi NaAanaN', 'suputamadre chaval', 'que guaaapo chaval',
               'Tranquilo.', 'las barracudas chaval', 'buah chaval me ha parado la policia','te pega un mordisco y te sale pelo chaval',
               'el octacore chaval','aroz chaval','esta bueno chaval','jojojo','Bueno. Tranquilo.','seliosxxx, diselo a tu prima']

def test_selios(message):
    if message.text:
        return 'chaval' in message.text

@bot.message_handler(func=test_selios)
def seliosxxx(message):
    text=selios_list[randint(0,len(selios_list)-1)]
    bot.send_message(message.chat.id,text)