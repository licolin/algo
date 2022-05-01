# -*- encoding: utf-8 -*-
# Author: li_colin
# 归并排序

def merge_sort(_list):
    if len(_list) <= 1:
        return _list
    mid = len(_list) // 2
    left = merge_sort(_list[:mid])
    right = merge_sort(_list[mid:])
    merge = []
    while left and right:
        if left[0] <= right[0]:
            merge.append(left.pop(0))
        else:
            merge.append(right.pop(0))
    merge.extend(left if left else right)
    print("merge is :", merge)
    return merge


print(merge_sort([1, 5, 2, 3, 6, 7, 10, 8, 19, 2, 15, 17, 11]))
