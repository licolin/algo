# -*- encoding: utf-8 -*-
# Author: li_colin
# 判断value in big list
# 最好办法是把big list转化为 dict
# list 转化为set 效率跟 dict 相当
stock = [1, 2, 3, 4, 5]
stock_ = dict(zip(stock, [True, ] * len(stock)))
_stock_ = set([i for i in stock])
