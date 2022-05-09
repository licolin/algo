# -*- encoding: utf-8 -*-
# Author: li_colin
# 二叉树
# 链表实现


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


bt = BinaryTree(1)
bt.insertRight(2)
bt.getRight().insertRight(3)
bt.getRight().insertLeft(6)
print(bt.data)
print(bt.right.left.data)
