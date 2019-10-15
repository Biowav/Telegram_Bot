from utils import *

insult_list2 = ['estas mas perdido que un hijoputa el dia del padre',
                'me vas a comer los tarzanetes del culo',
                'eres mas feo que pegar a un padre en navidad con un calcetin usado lleno de pilas alcalinas',
                'tu madre es tan gorda, que una vez se dio la vuelta en la cama y se cayo POR LOS DOS LADOS, la muy hipopotama',
                '\nCon los huesos de tus muertos\nme voy a hacer una escalera\npara subir al granero\ny follarme a tu abuela\n\n - Calderon de la Canoa',
                'si Cristo murió en la cruz con 3 clavos solamente, como no muere tu hermana que se la clava tanta gente.',
                'si lo que vas a decir no es más bonito que el silencio, entonces cállate',
                'me voy a cagar en tu puta madre n veces',
                'vete hacer gárgaras con la menstruación de tu puta madre']

insult_list = ['eres mas inutil que el ; en python',
               'eres mas inutil que los espacios en LATEX',
               'eres mas inutil que programar en ADA',
               'tu madre es tan gorda que necesita enteros de 128 bits para almacenar el peso',
               'eres mas inutil que calcular la inversa de la matriz identidad',
               'eres tan tonto que cuentas los elementos del conjunto VACIO',
               'eres mas feo que la inversa de f(X) = x^4+x^3+x^2+x+1 - https://www.wolframalpha.com/input/?i=inv(x%5E4%2Bx%5E3%2Bx%5E2%2Bx%2B1)',
               'el seno de tu pene es aproximadamente igual a tu pene',
               'eres tan tonto que le buscas las caras a una esfera',
               'eres mas inutil que el nobel de la paz',
               'eres mas asqueroso que un NullPointerException',
               'eres mas pesado que un while(true)',
               'eres peor que un windows vista',
               'eres tan tonto que ordenas una lista por backtracking',
               'eres mas asqueroso que un tensor',
               'eres mas debil que el campo en el interior de una esfera',
               'eres mas inutil que el gradiente de una funcion constate',
               'eres mas inutil que un filtro en corriente continua'

               ]


def test_insult(message):
    if message.text:
        return message.text[:16].lower() == 'gauss insulta a '

def test_destroy(message):
    if message.text:
        return message.text[:17].lower()== 'gauss destruye a '

@bot.message_handler(func=test_destroy)
def destroy(message):
    if message.text[16:].lower() == 'gauss':
        bot.reply_to(message, 'a insultar a tu puta madre')
    else:
        text = message.text[16:] + ' ' + insult_list2[randint(0, len(insult_list2) - 1)]
        bot.send_message(message.chat.id, text)

@bot.message_handler(func=test_insult)
def insult(message):
    if message.text[16:].lower() == 'gauss':
        bot.reply_to(message, 'a insultar a tu puta madre')
    else:
        text = message.text[16:] + ' ' + insult_list[randint(0, len(insult_list) - 1)]
        bot.send_message(message.chat.id, text)
