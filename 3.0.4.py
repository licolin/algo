# -*- encoding: utf-8 -*-
# Author: li_colin
# 十进制转二进制

class Stack:
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)

    def pop(self):
        if self.data:
            return self.data.pop()
        else:
            pass

    def isEmpty(self):
        return len(self.data) == 0


def dec2bin(val, base):
    digits = "0123456789ABCDEF"
    dec2stack = Stack()
    ret = ""
    while val:
        to_stack = val % base
        # python3 中 val/2 大概会有小数   val//2 表示整除
        val = val // base
        dec2stack.push(to_stack)
    while not dec2stack.isEmpty():
        ret += str(digits[dec2stack.pop()])
    return ret


print(dec2bin(28, 16))
