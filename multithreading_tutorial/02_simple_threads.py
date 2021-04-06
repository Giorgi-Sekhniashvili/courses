"""
makes 4 threads and run infinite while loop

concurrency: ability of a program to be broken into parts that can run independently of each other
- Program structure
- Dealing with multiple things at once
Parallel Execution: two or more tasks executing at the same time on a different CPUs
- Simultaneous execution
- Doing multiple things at once

GIL prevents multiple python threads to execute at the same time
"""
import os
import threading


def cpu_waster():
    i = 0
    while True:
        i += 1


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
