"""
used to utiliese more than one cpu
"""

import multiprocessing as mp
import threading
import os


def cpu_waster():
    i = 0
    while True:
        i += 1

print('__name__ = ', __name__)

# this if is needed so subprocesses doesn't create their subprocesses
if __name__ == '__main__':
    print('\n Process ID', os.getpid())
    print('Tread Count: ', threading.active_count())
    for thread in threading.enumerate():
        print(thread)

    print('\n starting 4 cpu_waster')
    for i in range(4):
        mp.Process(target=cpu_waster).start()

    print('\n Process ID', os.getpid())
    print('Tread Count: ', threading.active_count())
    for thread in threading.enumerate():
        print(thread)

