import os
import threading


def cpu_waster():
    while True:
        pass


print('\n Process ID', os.getpid())
print('Tread Count: ', threading.active_count())
for thread in threading.enumerate():
    print(thread)

print('\n starting 4 CPU wasters ...')
for i in range(4):
    threading.Thread(target=cpu_waster).start()

print('\n Process ID', os.getpid())
print('Tread Count: ', threading.active_count())
for thread in threading.enumerate():
    print(thread)
