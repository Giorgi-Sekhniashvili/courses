import threading

chopstick_a = threading.Lock()
chopstick_b = threading.Lock()
chopstick_c = threading.Lock()

sushi_count = 5000


def philosopher(name, first_chopstick: threading.Lock, second_chopstick: threading.Lock):
    global sushi_count
    sushi_eaten = 0

    while sushi_count > 0:
        with first_chopstick:
            with second_chopstick:
                if sushi_count > 0:
                    sushi_count -= 1
                    sushi_eaten += 1
                    print(name, 'took a piece! Sushi remaining: ', sushi_count)

    print(name, 'has eaten ', sushi_eaten, ' sushies')


if __name__ == '__main__':
    for i in range(50):
        threading.Thread(target=philosopher, args=('Gela', chopstick_a, chopstick_b)).start()
        threading.Thread(target=philosopher, args=('Bela', chopstick_a, chopstick_b)).start()
        threading.Thread(target=philosopher, args=('Mela', chopstick_a, chopstick_b)).start()
