import threading
import time


# same as set the target to a function
class MySubThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        # the target function
        print('in MySubThread ...')
        time.sleep(3)
        print("MySubThread has done it's job")


if __name__ == '__main__':
    print('declare my_subthread')
    my_sub_thread = MySubThread()

    print('start the thread')
    my_sub_thread.start()

    time.sleep(0.5)

    print('waiting for the sub_thread to finish')
    my_sub_thread.join()

    print('both done')