# -*- encoding: utf-8 -*-
# Author: li_colin
# 博物馆大盗
# 总物件一共是5件,总质量是 20 求取能盗取物件最大价值
# 动态规划实现

#  ---------------------------
# - item -- weight -- value --
# ----------------------------
# - 1 ------- 2 --------3-----
# - 2 ------- 3 --------4-----
# - 3 ------- 4 --------8-----
# - 4 ------- 5 --------8-----
# - 1 ------- 9 --------10----

weights = [0, 2, 3, 4, 5, 9]
value = [0, 3, 4, 8, 8, 10]

ret = [[0 for i in range(21)] for j in range(6)]


for i in range(1, 6):
    for j in range(1, 21):
        if weights[i] > j:
            ret[i][j] = ret[i - 1][j]
        else:
            ret[i][j] = max(ret[i - 1][j], (ret[i - 1][j - weights[i]] + value[i]))
# for ele in ret:
print(ret[5][20])
