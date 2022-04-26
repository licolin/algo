# -*- encoding: utf-8 -*-
# Author: li_colin
# 一群人,循环报数,报到特定数的人出列,求解最后剩下的人是谁

class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, val):
        self.data.insert(0, val)

    def dequeue(self):
        return self.data.pop()

    def isEmpty(self):
        return self.data == []

    def pop_val(self, i):
        return self.data.pop(i)

    def size(self):
        return len(self.data)


users = ["a", "b", "d", "e", "f", "h", "i"]


# 队列做法
def queue_method(val, num):
    _queue = Queue()
    for ele in val:
        _queue.enqueue(ele)
    i = 0
    while _queue.size() > 1:
        i += 1
        if i % num == 0:
            _queue.dequeue()
        else:
            tmp = _queue.dequeue()
            _queue.enqueue(tmp)
    return _queue.dequeue()


# list操作解法
def get_last_one(_users, num):
    while len(_users) > 1:
        if len(_users) > num:
            _users = _users[num:] + _users[0:num - 1]
        elif len(_users) == num:
            _users = _users[0:num - 1]
        else:
            if num % len(_users) == 0:
                _users.pop()
            else:
                _users.pop(num % len(_users) - 1)
    return _users[0]


print(get_last_one(users, 3))

print(queue_method(users, 3))
