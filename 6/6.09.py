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
        self.parent = None

    def hasLeftChild(self):
        return self.left

    def hasRightChild(self):
        return self.right


class BST:
    def __init__(self):
        self.root = None
        self.current = None

    def insertNode(self, node):
        if self.root is None:
            self.root = node
            node.parent = None
        else:
            self.put(node, self.root)

    # @staticmethod
    def put(self, node, root):
        if node.key < root.key:
            if root.hasLeftChild():
                self.put(node, root.hasLeftChild())
            else:
                root.left = node
                node.parent = root
        else:
            if root.hasRightChild():
                self.put(node, root.hasRightChild())
            else:
                root.right = node
                node.parent = root


bst = BST()
bst.insertNode(Node(12, 1))
bst.insertNode(Node(8, 5))
bst.insertNode(Node(15, 7))
bst.insertNode(Node(19, 20))
print(bst.root.right.right.key)
