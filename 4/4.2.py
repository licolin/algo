# -*- encoding: utf-8 -*-
# Author: li_colin
# 括号匹配
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


def single_match(val):
    dic = {"<": ">", "(": ")", "{": "}", "[": "]"}
    st = Stack()
    for ele in val:
        if ele in dic:
            st.push(ele)
        else:
            if st.isEmpty() or not ele == dic[st.pop()]:
                return False
    if st.isEmpty():
        return True
    else:
        return False


print(single_match("<>{()}[]"))
