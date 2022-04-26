# -*- encoding: utf-8 -*-
# Author: li_colin
# 硬币兑换 算法
# 硬币币种有(1,5,10,25), 需要兑换的钱是63


def money_exchange(changes, val, pre_ret):
    min_coin = val
    if val in changes:
        pre_ret[val] = 1
        return 1
    if pre_ret[val]:
        return pre_ret[val]
    for ele in [c for c in changes if c <= val]:
        coins = 1 + money_exchange(changes, val - int(ele), pre_ret)
        if coins < min_coin:
            min_coin = coins
            pre_ret[val] = min_coin
    return min_coin


print(money_exchange([1, 5, 10, 25], 63, [0] * 64))
