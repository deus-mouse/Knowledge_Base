'''оповестит если изменить размер окна
запускать в ТЕРМИНАЛЕ!'''

import signal
import time
import sys

def resize_handler(signum, frame):
    print ("Window was resized")


signal.signal(signal.SIGWINCH, resize_handler)

while True:
    print("Hey")
    time.sleep(1)