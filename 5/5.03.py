# -*- encoding: utf-8 -*-
# Author: li_colin
# 冒泡排序
# 选择排序
# 插入排序
# 希尔排序

def bubble_sort(lists):
    for i in range(len(lists)):
        for j in range(len(lists) - i - 1):
            if lists[j + 1] < lists[j]:
                lists[j], lists[j + 1] = lists[j + 1], lists[j]
    return lists


print(bubble_sort([1, 3, 2, 5, 9, 4, 2]))


def select_sort(lists):
    for i in range(len(lists)):
        position = 0
        for j in range(len(lists) - i - 1):
            if lists[j + 1] > lists[position]:
                position = j + 1
        lists[position], lists[len(lists) - i - 1] = lists[len(lists) - i - 1], lists[position]
    return lists


print(select_sort([1, 3, 2, 5, 9, 4, 2]))


def insert_sort(lists):
    for i in range(1, len(lists)):
        position = i
        while position > 0 and lists[position] < lists[position - 1]:
            lists[position], lists[position - 1] = lists[position - 1], lists[position]
            position = position - 1
    return lists


print(insert_sort([1, 3, 2, 5, 9, 4, 2]))


def shell_sort(lists):
    def shell_insert(start, lists, n):
        for i in range(start, len(lists), n):
            position = i
            while position > start and lists[position] < lists[position - n]:
                lists[position], lists[position - n] = lists[position - n], lists[position]
                position = position - n

    gap = len(lists) // 2
    while gap:
        for j in range(2):
            shell_insert(j, lists, gap)
        gap = gap // 2
    return lists


print(shell_sort([1, 3, 2, 5, 9, 4, 2, 10, 56, 18, 15, 66, 12]))