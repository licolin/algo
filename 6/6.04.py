# -*- encoding: utf-8 -*-
# Author: li_colin
# 二叉树
# 链表实现

# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None


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


bt = BinaryTree(1)
bt.insertRight(2)
bt_r = bt.getRight()
bt_r.insertRight(3)
bt_r.insertLeft(6)
print(bt.data)
print(bt.right.left.data)
