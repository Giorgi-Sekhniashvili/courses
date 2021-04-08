"""
Each member is waiting for another member to take action

Liveliness:
- Properties that require a system to make progress
- Members may have to "take turns" in critical sections

Ensure Lock() - ordering
"""

import threading

chopstick_a = threading.Lock()
chopstick_b = threading.Lock()
chopstick_c = threading.Lock()

sushi_count = 500


def philosopher(name, first_chopstick: threading.Lock, second_chopstick: threading.Lock):
    global sushi_count

    while sushi_count > 0:
        first_chopstick.acquire()
        second_chopstick.acquire()
        try:
            if sushi_count > 0:
                sushi_count -= 1
                print(name, 'took a piece! Sushi remaining: ', sushi_count)
            if sushi_count == 10:
                print(1/0)
        finally:
            second_chopstick.release()
            first_chopstick.release()


if __name__ == '__main__':
    threading.Thread(target=philosopher, args=('Gela', chopstick_a, chopstick_b)).start()
    threading.Thread(target=philosopher, args=('Bela', chopstick_b, chopstick_c)).start()
    threading.Thread(target=philosopher, args=('Mela', chopstick_a, chopstick_c)).start()
