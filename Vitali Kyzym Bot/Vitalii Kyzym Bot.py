import telepot
from telepot.loop import MessageLoop
import time

bot = telepot.Bot('859146216:AAHb_DkF6mQ44aLR9ElHsM0HY1t0OK_way0')

def handle(msg):
    print(msg["text"])

MessageLoop(bot, handle).run_as_thread()

while 1:
    time.sleep(1)
