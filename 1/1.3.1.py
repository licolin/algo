# -*- encoding: utf-8 -*-
# Author: li_colin
# 求最大子序列 暴力解法

def get_list():
    import random
    a = range(-50, 50)
    return random.sample(a, 25)


def get_min_sub_list(master_list, n):
    ret_sum = 0
    for i in range(n):
        sub_sum, temp_sum = master_list[i], master_list[i]
        for j in range(i + 1, n):
            temp_sum = temp_sum + master_list[j]
            sub_sum = temp_sum if temp_sum >= sub_sum else sub_sum
        ret_sum = sub_sum if sub_sum > ret_sum else ret_sum
    return ret_sum


print("mas sub list sum is:", get_min_sub_list(get_list(), 15))
