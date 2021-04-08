import threading
from readerwriterlock import rwlock

WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

today = 0

# marker = threading.Lock()
marker = rwlock.RWLockFair()


def calendar_reader(id_number):
    global today
    name = 'Reader - ' + str(id_number)

    read_marker = marker.gen_rlock()
    while today < len(WEEKDAYS) - 1:
        read_marker.acquire()
        print(name, ' sees that today is ', WEEKDAYS[today], ' readers count = ', read_marker.c_rw_lock.v_read_count)
        read_marker.release()


def calendar_writer(id_number):
    global today
    name = 'Writer - ' + str(id_number)

    write_marker = marker.gen_wlock()
    while today < len(WEEKDAYS) - 1:
        write_marker.acquire()
        today = (today + 1) % 7
        print(name, 'updated date to ', WEEKDAYS[today])
        write_marker.release()


if __name__ == '__main__':
    for i in range(10):
        threading.Thread(target=calendar_reader, args=(i,)).start()

    for i in range(2):
        threading.Thread(target=calendar_writer, args=(i,)).start()
