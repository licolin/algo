# -*- encoding: utf-8 -*-
# Author: li_colin
# stack

class Stack:
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)

    def pop(self):
        return self.data.pop()


class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, val):
        self.data.insert(0, val)

    def dequeue(self):
        return self.data.pop()
