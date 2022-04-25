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

total = 20
elements = {(2, 3), (3, 4), (4, 8), (5, 8), (9, 10)}


def solution(args, c):
    m = {}

    def get_value(val, t):
        if t == 0 or not val:
            return 0
        if t in m:
            return m[t]
        else:
            _max = 0
            for ele in val:
                if ele[0] <= t:
                    tmp = get_value(val - {ele}, t - ele[0]) + ele[1]
                    _max = max(tmp, _max)
            m[tuple(val), t] = _max
        return _max

    return get_value(args, c)


print(solution(elements, 20))
