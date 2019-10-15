from utils import *
list_class_members=[173307110,176013691,
236834006,
15448936,
12661796,
54269381,
2282100,
11602094,
274760134,
293878948,
258600031,
60321447,
182830817,
134241736,
59123141,
216241172,
374980081,
64379817,
265626272
]
def haritz_speaks(message):
    if message.text:
        return message.from_user.id==169540342 and 'gauss.kick()' in message.text.lower()

@bot.message_handler(func=haritz_speaks)
def haritz_function(message):
    bot.kick_chat_member(message.chat.id,list_class_members[randint(0,len(list_class_members)-1)])