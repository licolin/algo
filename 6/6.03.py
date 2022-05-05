# -*- encoding: utf-8 -*-
# Author: li_colin
# 二叉树
# 列表实现


class BinaryTree:
    def __init__(self):
        pass

    @staticmethod
    def create_tree(a):
        return [a, [], []]

    @staticmethod
    def insertLeft(tree, val):
        left = tree.pop(1)
        if len(left) > 1:
            tree.insert(1, [val, left, []])
        else:
            tree.insert(1, [val, [], []])

    @staticmethod
    def insertRight(tree, val):
        right = tree.pop(2)
        if len(right) > 1:
            tree.insert(2, [val, [], right])
        else:
            tree.insert(2, [val, [], []])

    @staticmethod
    def getLeftChild(tree):
        return tree[1]

    @staticmethod
    def getRightChild(tree):
        return tree[2]


bt = BinaryTree()

first = bt.create_tree(1)
print(first)
bt.insertLeft(first, 2)
bt.insertRight(first, 6)
bt.insertRight(first, 3)
bt.insertLeft(first, 5)
first_left = bt.getLeftChild(first)
print("first_left ", first_left, len(first_left), sep="::")
print(first)
bt.insertRight(first_left, 10)
print(first)
