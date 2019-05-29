import telepot
from telepot.loop import MessageLoop
import time

bot = telepot.Bot('874633254:AAEKR5m_ZL6mJ83VQIslrJcastFLaRr96CQ')  

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if msg["text"] == "Hi":
        bot.sendMessage(chat_id, 'Hello!')
    elif msg["text"] == "bye" :
        bot.sendMessage(chat_id, 'Bai Kawaii Chan!')

MessageLoop(bot, handle).run_as_thread()

while 1:
    time.sleep(1)
