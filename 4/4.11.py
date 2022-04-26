# -*- encoding: utf-8 -*-
# Author: li_colin
# 硬币兑换 算法 动态规划实现
# 硬币币种有(1,5,10,25), 需要兑换的钱是63


def money_exchange(changes, val, pre_ret):
    for i in range(1, val + 1):
        if i in changes:
            pre_ret[i] = 1
        min_coins = val
        for ele in [c for c in changes if i >= c]:
            tmp = 1 + pre_ret[i - ele]
            if tmp < min_coins:
                pre_ret[i] = tmp
                min_coins = tmp
    return pre_ret[val]


print(money_exchange([1, 5, 10, 21, 25], 63, [0] * 64))
