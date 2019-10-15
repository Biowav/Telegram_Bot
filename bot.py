from utils import *
import listener
importdir.do('plugins',globals())
db=dbhelper.DBHelper()
db_id_username=db.db_to_list()
bot.set_update_listener(listener.listener)
while 1:
    time.sleep(1)
    try:
        print("OK")
        bot.polling(none_stop=True)
        print("END")
    except Exception:
        print("ERROR")
        continue
    break
