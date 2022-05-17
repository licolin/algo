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

    def hasBothChild(self):
        return self.left is not None and self.right is not None

    def hasOnlyLeftChild(self):
        return self.left is not None and self.right is None

    def hasOnlyRightChild(self):
        return self.right is not None and self.left is None

    def isLeaf(self):
        return self.left is None and self.right is None


class BST:
    def __init__(self):
        self.root = None

    def insertNode(self, node):
        if self.root is None:
            self.root = node
            node.parent = None
        else:
            self.put(node, self.root)

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

    def iter(self, root):
        print(root.val)
        if root.hasLeftChild():
            self.iter(root.hasLeftChild())
        if root.hasRightChild():
            self.iter(root.hasRightChild())

    def get(self, root, key):
        if root.key == key:
            return root
        if root.hasLeftChild() and key < root.key:
            return self.get(root.hasLeftChild(), key)
        elif root.hasRightChild() and key > root.key:
            return self.get(root.hasRightChild(), key)
        else:
            return None

    def delete(self, root, key):
        node = self.get(root, key)
        if node.isLeaf():
            if node.parent.left == node:
                node.parent.left = None
            elif node.parent.right == node:
                node.parent.right = None
        elif node.hasOnlyLeftChild():
            node.parent.left = node.left
            node.left.parent = node.parent
        elif node.hasOnlyRightChild():
            node.parent.right = node.right
            node.right.parent = node.parent
        elif node.hasBothChild():
            _node = self.findMin(node)
            if _node:
                node.key = _node.key
                node.val = _node.val
                self.delete(_node, _node.key)

    def findMin(self, root):
        if root.isLeaf():
            return root
        if root.hasLeftChild():
            return self.findMin(root.hasLeftChild())


bst = BST()
bst.insertNode(Node(12, 1))
bst.insertNode(Node(8, 5))
bst.insertNode(Node(15, 7))
bst.insertNode(Node(19, 20))
print("not delete")
bst.iter(bst.root)
bst.delete(bst.root, 12)
print("delete")
bst.iter(bst.root)
