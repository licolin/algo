# -*- encoding: utf-8 -*-
# Author: li_colin
# 有序链表


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


class OrderList:
    def __init__(self):
        self.head = None

    def addNode(self, node):
        tmp = self.head
        if tmp is None or tmp.data >= node.data:
            self.head = node
            node.SetNext(tmp)
        else:
            node_next = tmp.GetNextNode()
            while node_next is not None:
                if tmp.data <= node.data <= node_next.data:
                    tmp.next = node
                    node.next = node_next
                    break
                else:
                    tmp = node_next
                    node_next = tmp.next
            if node_next is None:
                tmp.next = node

    def search(self, val):
        tmp = self.head
        _isFind = False
        stop = False
        if tmp.data > val:
            return False
        while not stop and tmp is not None:
            if tmp.data == val:
                return True
            else:
                tmp = tmp.next
                if tmp.data < val:
                    return False
        return _isFind

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


_order_list = OrderList()
_order_list.addNode(Node(100))
_order_list.addNode(Node(98))
_order_list.addNode(Node(99))
_order_list.addNode(Node(102))

_order_list.iterate()
print(_order_list.search(99))
_order_list.removeNode(102)
_order_list.iterate()

