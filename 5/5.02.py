# -*- encoding: utf-8 -*-
# Author: li_colin
# 二分查找

def binary_search(lists, item):
    start = 0
    end = len(lists) - 1
    found = False
    while start <= end:
        mid = (start + end) // 2
        if lists[mid] == item:
            found = True
            return mid, found
        else:
            if lists[mid] < item:
                start = mid + 1
            else:
                end = mid - 1
    return 0, False


print(binary_search([1, 2, 3, 4, 5], 5))
