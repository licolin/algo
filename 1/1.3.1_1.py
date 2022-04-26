# -*- encoding: utf-8 -*-
# Author: li_colin
# 求最大子序列 O(n) 解法

def get_list():
    import random
    a = range(-50, 50)
    return random.sample(a, 15)


def get_min_sub_list(master_list, n):
    sub_max = 0
    temp_sum = 0
    for i in range(n):
        temp_sum += master_list[i]
        if temp_sum < 0:
            temp_sum = 0
        else:
            sub_max = temp_sum if temp_sum > sub_max else sub_max
    return sub_max


print("mas sub list sum is:", get_min_sub_list(get_list(), 15))
