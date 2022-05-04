# -*- encoding: utf-8 -*-
# Author: li_colin
# 快速排序

def quick_sort(lists):
    def helper(li, start, end):
        if end > start:
            part = split_list(li, start, end)
            helper(li, start, part - 1)
            helper(li, part + 1, end)

    def split_list(lis, start, end):
        left = start + 1
        right = end
        while left <= right:
            while left <= right and lis[left] <= lis[start]:
                left = left + 1
            while lis[right] >= lis[start] and left <= right:
                right = right - 1
            if left <= right:
                lis[left], lis[right] = lis[right], lis[left]
                left = left + 1
                right = right - 1

        lis[start], lis[right] = lis[right], lis[start]
        return right

    helper(lists, 0, len(lists) - 1)
    return lists


print(quick_sort([8, 5, 2, 3, 6, 7, 8, 10, 19, 2, 15, 17, 11]))
