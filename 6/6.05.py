# -*- encoding: utf-8 -*-
# Author: li_colin
# 二叉树解析算术运算表达式
# for example  (3+(5*6))

class BinaryTree:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

    def insertLeft(self, val):
        _node = BinaryTree(val)
        if self.left:
            tmp = self.left
            self.left = _node
            _node.left = tmp
        else:
            self.left = _node

    def insertRight(self, val):
        _node = BinaryTree(val)
        if self.right:
            tmp = self.right
            self.right = _node
            _node.right = tmp
        else:
            self.right = _node

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setRootVal(self, val):
        self.data = val

    def getRootVal(self):
        return self.data


class Stack:
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)

    def pop(self):
        return self.data.pop()


str_fmt = "(3+(5*6))"
chars = [i for i in str_fmt]


# (3+(5*6))
def gen_tree(_chars):
    t_stack = Stack()
    bt = BinaryTree("")
    t_stack.push(bt)
    _currentTree = bt
    for ele in _chars:
        if ele == "(":
            _currentTree.insertLeft("")
            t_stack.push(_currentTree)
            _currentTree = _currentTree.getLeft()
        elif ele not in ("+", "-", "*", "/", ")"):
            _currentTree.setRootVal(int(ele))
            _currentTree = t_stack.pop()
        elif ele in ("+", "-", "*", "/"):
            _currentTree.setRootVal(ele)
            _currentTree.insertRight("")
            t_stack.push(_currentTree)
            _currentTree = _currentTree.getRight()

        elif ele == ")":
            _currentTree = t_stack.pop()
        else:
            pass
    return bt


print(gen_tree(_chars=chars))
