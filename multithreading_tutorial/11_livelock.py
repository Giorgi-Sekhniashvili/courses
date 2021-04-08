"""
Multiple threads or processes ar actively responding to each other to resolve conflict,
but that prevents them from making progress

- you eat!
- no you!
- no you!
- no you!
"""

import threading
import time
from random import random

sushi_count = 500

chopstick_a = threading.Lock()
chopstick_b = threading.Lock()
chopstick_c = threading.Lock()


def philosopher(name, first_chopstick: threading.Lock, second_chopstick: threading.Lock):
    global sushi_count

    while sushi_count > 0:
        first_chopstick.acquire()
        if not second_chopstick.acquire(blocking=False):
            print(name, ' released their first chopstick.')
            first_chopstick.release()
            time.sleep(random()/10)     # solution for livelock
        else:
            try:
                if sushi_count > 0:
                    sushi_count -= 1
                    print(name, ' took a piece, sushi remaining: ', sushi_count)
            finally:
                second_chopstick.release()
                first_chopstick.release()

if __name__ == '__main__':
    threading.Thread(target=philosopher, args=('Gela', chopstick_a, chopstick_b)).start()
    threading.Thread(target=philosopher, args=('Bela', chopstick_b, chopstick_c)).start()
    threading.Thread(target=philosopher, args=('Mela', chopstick_c, chopstick_a)).start()



