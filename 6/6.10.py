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
            if factor > 1 and key < root.left.key:
                return self.r_rotation(root)
            if factor > 1 and key > root.left.key:
                t = self.l_rotation(root.left)
                return self.r_rotation(root)
            if factor < -1 and key > root.right.key:
                return self.l_rotation(root)
            if factor < -1 and key < root.right.key:
                t = self.r_rotation(root.right)
                return self.l_rotation(root)
            return root

    def r_rotation(self, root):
        tmp = root.left
        tmp_sub = tmp.right
        tmp.right = root
        root.left = tmp_sub
        tmp.height = self.getHeight(tmp)
        tmp.right.height = self.getHeight(tmp.right)
        return tmp

    def l_rotation(self, root):
        tmp = root.right
        tmp_sub = tmp.left
        root.right = tmp_sub
        tmp.left = root
        tmp.height = self.getHeight(tmp)
        tmp.left.height = self.getHeight(tmp.left)
        return tmp

    def get_balance(self, root):
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getHeight(self, root):
        if root is None:
            return 0
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
