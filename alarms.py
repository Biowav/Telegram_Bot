import schedule
import time
from utils import bot
def job():
    bot.send_message(chat_id=-219419208,text='POLE PROGRAMADA A LAS 18:00')
    bot.send_message(chat_id=-219419208,text='POLE PROGRAMADA A LAS 18:00')
    bot.send_message(chat_id=-219419208,text='POLE PROGRAMADA A LAS 18:00')


schedule.every().day.at("11:52").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)