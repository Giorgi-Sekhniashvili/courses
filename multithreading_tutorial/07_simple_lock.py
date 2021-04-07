import time
import threading

count = 0
lock = threading.Lock()


def adder():
    global count
    for i in range(5):
        print(threading.current_thread().getName(), ' is thinking')
        time.sleep(0.5)
        lock.acquire()
        count += 1
        lock.release()


if __name__ == '__main__':
    thread_one = threading.Thread(target=adder, name='thread_one')
    thread_two = threading.Thread(target=adder, name='thread_two')

    thread_one.start()
    thread_two.start()

    thread_one.join()
    thread_two.join()

    print('count = ', count)
