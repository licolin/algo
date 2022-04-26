# -*- encoding: utf-8 -*-
# Author: li_colin

# 双端队列
# 判断回文串

class Deque:
    def __init__(self):
        self.data = []

    def addRear(self, val):
        self.data.append(val)

    def addFront(self, val):
        self.data.insert(0, val)

    def popRear(self):
        return self.data.pop()

    def popFront(self):
        return self.data.pop(0)

    def isEmpty(self):
        return self.data == []

    def size(self):
        return len(self.data)


def checkPalindrome(val):
    _deque = Deque()
    for ele in val:
        _deque.addFront(ele)
    is_palindrome = True
    while _deque.size() > 1 and is_palindrome:
        rear = _deque.popRear()
        front = _deque.popFront()
        if rear != front:
            is_palindrome = False
    return is_palindrome


print(checkPalindrome("123"))
