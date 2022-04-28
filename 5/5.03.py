# -*- encoding: utf-8 -*-
# Author: li_colin
# 冒泡排序
# 选择排序
# 插入排序

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

lists = [1, 2]
lists.insert(2, 3)
print(lists)


def insert_sort(lists):
    ret = []
    for ele in lists:
        if len(ret) < 2:
            if not ret:
                ret.append(ele)
            else:
                if ele <= ret[0]:
                    ret.insert(0, ele)
                else:
                    ret.insert(1, ele)
        else:
            if ele <= ret[0]:
                ret.insert(0, ele)
            elif ele >= ret[len(ret) - 1]:
                ret.insert(len(ret), ele)
            else:
                for r in range(len(ret) - 1):
                    if ret[r] <= ele <= ret[r + 1]:
                        ret.insert(r + 1, ele)
                        # 跳出这层循环
                        break

    return ret


print(insert_sort([1, 3, 2, 5, 9, 4, 2]))
