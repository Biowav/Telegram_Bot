from utils import *
count=2;

@bot.message_handler(func= lambda message: message.from_user.username is None and not message.from_user.id==64379817)
def no_username(message):
    global count

    if count==0:
        bot.send_message(message.chat.id,"Ponte username 1 aviso")
        count=1
    elif count==1:

        
        bot.send_message(message.chat.id, "Ponte username 2 aviso")
        count = 2
    elif count==2:
        count = 0
        bot.send_message(chat_id=message.chat.id, text="Te avise, estas <b>fuera</b>",parse_mode="HTML")
        bot.kick_chat_member(message.chat.id,message.from_user.id)
