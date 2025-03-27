### src/dungeons/utils.py
import sys
import time
import os

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause(secs):
    time.sleep(secs)
