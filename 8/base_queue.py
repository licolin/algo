# -*- encoding: utf-8 -*-
# Author: li_colin

import multiprocessing
from multiprocessing import queues
import sys


class SharedCounter:

    def __init__(self, n=0):
        self.count = multiprocessing.Value("i", n)

    def increment(self, n=1):
        """Increment the counter by n (default = 1)"""
        with self.count.get_lock():
            self.count.value += n

    @property
    def value(self):
        """Return the value of the counter"""
        return self.count.value


class Queue(queues.Queue):

    def __init__(self, *args, **kwargs):
        if sys.version_info < (3, 0):
            super(Queue, self).__init__(*args, **kwargs)
        else:
            super(Queue, self).__init__(
                *args, ctx=multiprocessing.get_context(), **kwargs
            )
        self.size = SharedCounter(0)

    def __getstate__(self):
        return super(Queue, self).__getstate__() + (self.size,)

    def __setstate__(self, state):
        super(Queue, self).__setstate__(state[:-1])
        self.size = state[-1]

    def put(self, *args, **kwargs):
        super(Queue, self).put(*args, **kwargs)
        self.size.increment(1)

    def get(self, *args, **kwargs):
        x = super(Queue, self).get(*args, **kwargs)
        self.size.increment(-1)
        return x

    def qsize(self) -> int:
        """Reliable implementation of multiprocessing.Queue.qsize()"""
        return self.size.value

    def empty(self) -> bool:
        """Reliable implementation of multiprocessing.Queue.empty()"""
        return not self.qsize() > 0
