import telepot
from telepot.loop import MessageLoop
import time

bot = telepot.Bot('874633254:AAEKR5m_ZL6mJ83VQIslrJcastFLaRr96CQ')

def handle(msg):
    if msg["text"] == "Hi":
        print("get out of my face")
    print(msg["text"])

MessageLoop(bot, handle).run_as_thread()

while 1:
    time.sleep(1)
