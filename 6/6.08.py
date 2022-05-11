# -*- encoding: utf-8 -*-
# Author: li_colin
# heap 堆

class BinaryHeap:
    def __init__(self):
        self.data = [0]
        self.current = 0

    def insertHeap(self, val):
        self.data.append(val)
        self.current = self.current + 1
        self.upCompare(self.current)

    def upCompare(self, i):
        index = i
        parent = index // 2
        while parent:
            if self.data[index] < self.data[parent]:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
            else:
                pass
            index = parent
            parent = index // 2

    # 根节点最小 删除根节点 重构堆
    def delMin(self):
        if self.current:
            self.data[1], self.data[self.current] = self.data[self.current], self.data[1]
            self.data.pop()
            self.current = self.current - 1
            i = 1
            while i <= self.current:
                i = self.downCompare(i)

    def downCompare(self, i):
        index = 2 * i
        if 2 * i + 1 <= self.current:
            index = 2 * i if self.data[2 * i] < self.data[2 * i + 1] else 2 * i + 1
            if self.data[i] > self.data[index]:
                self.data[i], self.data[index] = self.data[index], self.data[i]
        elif 2 * i == self.current:
            self.data[i], self.data[2 * i] = self.data[2 * i], self.data[i]
        else:
            pass
        return index


bh = BinaryHeap()
bh.insertHeap(1)
bh.insertHeap(29)
bh.insertHeap(12)
bh.insertHeap(3)
bh.insertHeap(9)
bh.insertHeap(8)
bh.insertHeap(2)
bh.insertHeap(7)
bh.insertHeap(6)
bh.insertHeap(21)
# bh.insertHeap(20)
print(bh.data)
bh.delMin()
bh.delMin()
print(bh.data)
