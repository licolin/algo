# -*- encoding: utf-8 -*-
# Author: li_colin

# 二分查找
# 递归解法

def binary_search(lists, item):
    if len(lists) == 0:
        return False
    else:
        mid = len(lists) // 2
        if lists[mid] == item:
            return True
        else:
            if lists[mid] < item:
                return binary_search(lists[mid + 1:], item)
            else:
                return binary_search(lists[:mid], item)


print(binary_search([1, 2, 3, 4, 5], 4))
