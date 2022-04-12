# -*- encoding: utf-8 -*-
# Author: li_colin
# 很好的栗子
# 模拟打印机队列 在不同的打印模式下(粗打,精打),模拟出用户需要等待的时间.
import random


class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, val):
        self.data.insert(0, val)

    def dequeue(self):
        return self.data.pop()

    def isEmpty(self):
        return self.data == []

    def numOfMember(self):
        return len(self.data)


class PrintClass:
    def __init__(self, ppm):
        self.ppm = ppm
        self.currentTask = None
        self.remainTime = 0

    def busy(self):
        if self.currentTask is None:
            return False
        else:
            return True

    def tick(self):
        if self.currentTask:
            self.remainTime = self.remainTime - 1
            if self.remainTime <= 0:
                self.currentTask = None

    def startNewTask(self, _new_task):
        self.currentTask = _new_task
        self.remainTime = _new_task.getPages() * 60 / self.ppm


class Task:
    def __init__(self, time_now, pages):
        self.timestamp = time_now
        self.pages = pages

    def getPages(self):
        return self.pages

    def waitTime(self, current_time):
        return current_time - self.timestamp


def createTaskOrNot():
    num = random.randint(0, 180)
    if num == 50:
        return True
    else:
        return False


def simulate(ppm):
    queue = Queue()
    printer = PrintClass(ppm)
    sum_time = 0
    for i in range(3600):
        if createTaskOrNot():
            page = random.randint(1, 21)
            task = Task(i, page)
            queue.enqueue(task)
        if not queue.isEmpty() and not printer.busy():
            _task = queue.dequeue()
            printer.startNewTask(_task)
            sum_time += _task.waitTime(i)
            print("i --- ", i, _task.waitTime(i), " waiting task num is:", queue.numOfMember())
        printer.tick()
    print("sum time is:", sum_time)


simulate(5)
