from utils import *
def test_monumento(message):
    if message.text:
        return message.text[:10]=='!monumento'

@bot.message_handler(func=test_monumento)
def monumento(message):
    if message.text[:11]=='!monumento ':
        if message.text[11:] in monumento:
            bot.send_message(message.chat.id,monumento[message.text[11:]])
    else:
        monumento_list='\n'.join(['%s' % k for k in monumento.keys()])
        bot.send_message(message.chat.id,'Monumentos:\n'+monumento_list)



monumento={'OW':'menuda mieda el OW le van a dar bien por el culo. Solo he ganado una, ridiculo. Me mete con gente de nivel' \
                ' 600 y pone que son partidas con gente de tu misma habilidad un tio de 600 horas la misma habilidad que yo en 1h' \
                ' que le den por el culo no me vuelvo a comprar nada multijugador en mi vida que ascazo hostia puta. No tiene nada ' \
                ' es meterte a un online que no quiere que te guste el juego amargandote contra puta gente que te saca 70 niveles minimo.' \
                ' lo dejare ahi para que me recuerde mi tremenda estupidez. Cada vez que lo vea me acordare de igor y de su santa madre.',
        'reverte': '''Tome asiento. Voy a contarle cómo escapé perseguido de fuego y metralla de mi penúltima escaramuza.\n
Me lancé de la avioneta con tan solo un paracaídas y mis agallas. Me desbrocé contra el rocaje y levanté ileso, obviamente. Inicié mi marcha.\n
Vi enemigos, esos malasangres. Con un silbido imité un mirlo y conseguí rodearlos con maestría. Pero caí en la trampa de esos rufianes.\n
Debido a una hora ininterrumpida de golpes, perdí el conocimiento. Desperté en un sótano oscuro, atado a una silla y completamente desnudo.\n
Casi muerdo mi cápsula de cianuro, pero me dije a mi mismo: "Pérez-Reverte, los españoles no se rinden".
Mis músculos rajaron las ataduras.\n
Vinieron a por mi y tiré de mis oscuros tiempos como mercenario al servicio de la corona. Improvisé una espada ropera de madera con la silla.\n
Soy un maestro de la verdadera destreza, enseñé a esos malandrines mi bravura española y los desangré como los puercos que eran.\n
Al salir de la celda, ¡Horror! Una veintena de arcabuceros apuntaba a mi gallarda figura. Fallaron, por suerte, y yo visualicé mi objetivo.\n
Agarré a ese hideputa al que llamaban general y le hice volar sin alas precipicio abajo. Pero la arcabucería cargó otra salva de proyectiles\n
Corrí entre explosiones y árboles astillándose. Había cumplido mi misión. Ileso. Desnudo. Salvaje. Sanguinario. Español.''',
           'Stackoverflow':'http://stackoverflow.com/questions/15445285/how-can-i-connect-to-a-tor-hidden-service-using-curl-in-php'}
