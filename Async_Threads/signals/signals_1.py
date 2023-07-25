'''не даст отправить выполнение в бэкграунд командой CTRL+Z
запускать в ТЕРМИНАЛЕ!
https://www.youtube.com/watch?v=758tGjmp7Io'''



import signal
import time
import sys


def stop_handler(signum, frame):
    print("You cannot put me into the background!")


signal.signal(signal.SIGTSTP, stop_handler)

while True:
    print("Hey")
    time.sleep(1)

