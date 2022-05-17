# -*- encoding: utf-8 -*-
# Author: li_colin
# avl 树
# self banlanced bst tree

class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.height = None


class AVL:
    def __init__(self):
        pass

    def insert(self, root, key, val):
        if root is None:
            return TreeNode(key, val)
        else:
            if key < root.key:
                root.left = self.insert(root.left, key, val)
            else:
                root.right = self.insert(root.right, key, val)
            root.height = self.getHeight(root)
            factor = self.get_balance(root)

    def get_balance(self, root):
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getHeight(self, root):
        if root is None:
            return 0
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
