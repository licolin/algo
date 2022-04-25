# -*- encoding: utf-8 -*-
# Author: li_colin
# 博物馆大盗
# 总物件一共是5件,总质量是 20 求取能盗取物件最大价值
# 递归实现

#  ---------------------------
# - item -- weight -- value --
# ----------------------------
# - 1 ------- 2 --------3-----
# - 2 ------- 3 --------4-----
# - 3 ------- 4 --------8-----
# - 4 ------- 5 --------8-----
# - 1 ------- 9 --------10----

weights = [2, 3, 4, 5, 9]
value = [3, 4, 8, 8, 10]
total = 20


def get_value(val, w, t):
    # if t == 0:
    #     return 0
    # if t in weights:
    #     return value[weights.index(total)]
    # _max = 0
    # for ele in weights:
    #     if ele < t:
    #         tmp = get_value(weights.remove(ele))
    pass


print(get_value(value, weights, 20))
