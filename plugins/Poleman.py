from utils import *
def check_poleman(message):
    if message.text:
        if message.from_user.id==get_poleman_id() or message.from_user.id==father_id:
            return message.text[:6] =='!kill '
def check_poleman_user(message):
    if message.text:
        return message.text[:8] =='!poleman'
@bot.message_handler(func=check_poleman)
def poleman_kill(message):
    aux_db=dbhelper.DBHelper()
    for_user=aux_db.get_user_by_username(message.text[7:])
    if for_user:
        if for_user[0][1]==0:
            bot.reply_to(message,'Pues va a ser que no.')
            bot.kick_chat_member(message.chat.id,message.from_user.id)
        else:
            bot.kick_chat_member(message.chat.id,for_user[0][1])
    else:
        bot.send_message(message.chat.id,'No lo encuentro señor')

@bot.message_handler(func=check_poleman_user)
def get_poleman(message):
    aux_db=dbhelper.DBHelper()
    poleman_user=aux_db.get_username_by_id(get_poleman_id())[0][0]


    bot.send_message(message.chat.id,'<b>Poleman de hoy:</b> @'+poleman_user,parse_mode='HTML')
