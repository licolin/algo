# -*- encoding: utf-8 -*-
# Author: li_colin

from objprint import op


class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = self.getA()

    def getA(self):
        return self.a

    def setA(self, a):
        self.a = a


a = A("a", "b")
op(a)
