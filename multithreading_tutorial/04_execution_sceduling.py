import threading
import time
import os

chopping = True


def vegetable_chopper():
    name = threading.current_thread().getName()
    vegetable_count = 0

    while chopping:
        print(name, ' is chopping a vegetable')
        vegetable_count += 1

    print(name, ' chopped ', vegetable_count, ' vegetables.')


if __name__ == '__main__':
    threading.Thread(target=vegetable_chopper, name='first_thread').start()
    threading.Thread(target=vegetable_chopper, name='second_thread').start()

    time.sleep(2)
    chopping = False
