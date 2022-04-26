# -*- encoding: utf-8 -*-
# Author: li_colin

def printN(n):
    if n:
        printN(n - 1)
        print("n is ", n)


printN(100)
