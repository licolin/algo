# -*- encoding: utf-8 -*-
# Author: li_colin

import time


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


# Create and launch a thread
from threading import Thread

t = Thread(target=countdown, args=(10,))
t.start()

if t.is_alive():
    print('Still running')
else:
    print('Completed')
t.join()  #等待子线程执行完
print("main thread end!")
