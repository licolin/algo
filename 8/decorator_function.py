# -*- encoding: utf-8 -*-
# Author: li_colin

# function decorator
import time


def timeit(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = f(*args, **kwargs)
        print(time.time() - start)
        return ret

    return wrapper


@timeit
def my_func(x):
    time.sleep(x)


# my_func = timeit(my_func)
# timeit(my_func)(2)
# my_func(2)

