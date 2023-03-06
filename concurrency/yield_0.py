# -*- encoding: utf-8 -*-
# Author: li_colin

def numbers():
    i = 0
    while True:
        ret = yield i + 1  # “封存” 状态机状态
        print("ret ", ret)
        i += ret
        print(i)

def print_func(dic):
    print(dic)


n = numbers()  # 封存状态机初始状态
print("start ", n.send(None))  # 恢复封存的状态
print("5 ", n.send(5))
print("6 ", n.send(6))

# for i in range(10):
#     n.send(i)
