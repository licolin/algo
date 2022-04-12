# -*- encoding: utf-8 -*-
# Author: li_colin
# 链表
import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def SetData(self, data):
        self.data = data

    def GetData(self):
        return self.data

    def SetNext(self, node):
        self.next = node

    def GetNextNode(self):
        return self.next


class UnOrderList:
    def __init__(self):
        self.head = None

    def setHead(self, node):
        self.head = node

    def addNode(self, node):
        tmp = self.head
        self.head = node
        node.SetNext(tmp)

    def iterate(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.GetNextNode()

    def removeNode(self, data):
        if self.head.data == data:
            self.head = self.head.GetNextNode()
        else:
            previous = self.head
            current = previous.GetNextNode()
            while current:
                if current.data == data:
                    previous.next = current.GetNextNode()
                    break
                else:
                    previous = current
                    current = current.GetNextNode()


_un_order_list = UnOrderList()
_un_order_list.addNode(Node(89))
_un_order_list.addNode(Node(98))
_un_order_list.addNode(Node(99))
_un_order_list.addNode(Node(100))

_un_order_list.iterate()
_un_order_list.removeNode(99)
_un_order_list.iterate()
