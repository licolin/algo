# -*- encoding: utf-8 -*-
# Author: li_colin
import time


def WaitPosition(TimeOut):
    import time, random
    end = time.time() + TimeOut
    while True:
        if random.randint(1, 10000000) % 999999 == 0:
            return True, None
        elif time.time() > end:
            return False, "timeout"
        else:
            pass


print(time.time())
print(WaitPosition(1))
print(time.time())
