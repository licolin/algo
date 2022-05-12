# -*- encoding: utf-8 -*-
# Author: li_colin
# BST 二叉搜索树
# 性质  root 索引最小(最大),right_child索引left_child 索引

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.head = None
        self.current = None

    def insertNode(self, node):
        if self.head is None:
            self.head = node
            self.current = node
        else:
            pass


bst = BST()
