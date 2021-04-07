"""
data races are hard to debug
in order to prevent pay attention whenever two or more threads access the same resources
"""

import threading

count = 0


def adder(n_iters = 10_000_000):
    global count
    for i in range(n_iters):
        count += 1


if __name__ == '__main__':
    thread_one = threading.Thread(target=adder, name='thread_one')
    thread_two = threading.Thread(target=adder, name='thread_two')
    thread_three = threading.Thread(target=adder, name='thread_three')

    thread_one.start()
    thread_two.start()
    thread_three.start()

    thread_one.join()
    thread_two.join()
    thread_three.join()
    print('DONE! \n count = ', count)
