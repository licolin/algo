# -*- encoding: utf-8 -*-
# Author: li_colin
import time


class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        ret = self.func(*args, **kwargs)
        print(f"Time:{time.time() - start}")
        return ret


@Timer
def add(a, b):
    return a + b


print(add(2, 3))


class Timer1:
    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            start = time.time()
            ret = func(*args, **kwargs)
            print(f"{self.prefix}:{time.time()}")
            return ret

        return wrapper


@Timer1(prefix="current time:")
def add(a, b):
    return a + b


print("add(2, 3) :", add(2, 3))
