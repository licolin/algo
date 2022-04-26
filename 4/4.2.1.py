# -*- encoding: utf-8 -*-
# Author: li_colin
# 题目：
# 洗碗工小明碰上了一位强迫症老板老王，餐厅一共就10只盘子，老板给仔细编上了0～9等10个号码，并要求小明按照从0到9的编号来洗盘子，当然，每洗好一只盘子，就必须得整齐叠放起来。
# 小明洗盘子期间，经常就有顾客来取盘子，当然每位顾客只能从盘子堆最上面取1只盘子离开。老王在收银台仔细地记录了顾客依次取到盘子的编号，比如“1043257689”，这样他就能判断小明是不是遵照命令按照0123456789的次序来洗盘子了。你也能像老王一样作出准确的判断吗？

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

    def peek(self):
        return self.data[-1]


def pie_check(val):
    st = Stack()
    li = []
    for ele in val:
        for i in range(int(ele) + 1):
            if i not in li:
                st.push(i)
                li.append(i)
        if st.peek() == int(ele):
            st.pop()
    return st.isEmpty()


print(pie_check("4231078965"))
