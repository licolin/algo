# -*- encoding: utf-8 -*-
# Author: li_colin

# -*- encoding: utf-8 -*-
# Author: li_colin

from decimal import Decimal, ROUND_05UP, ROUND_HALF_UP
from _pydecimal import Decimal, Context, ROUND_HALF_UP


# 偶尔有效
def smart_round(x, n):
    return Decimal(x).quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)


# 严格四舍五入
def round2(n):
    precision = len(str(n).split(".")[0]) + 2
    return float(Context(prec=precision, rounding=ROUND_HALF_UP).create_decimal(str(n)))


# 垃圾
def round_up(value):
    return round(value * 100) / 100.0


print(smart_round(2.5, 0), " ", round2(2.5), " ", round_up(2.5))
print(smart_round(2.285, 2), " ", round2(2.285), " ", round_up(2.285))
print(smart_round(1.295, 2), " ", round2(1.295), " ", round_up(2.295))
print(smart_round(1.215, 2), " ", round2(1.215), " ", round_up(2.215))
print(smart_round(1.255, 2), " ", round2(1.255), " ", round_up(2.255))
print(smart_round(1.245, 2), " ", round2(1.245), " ", round_up(2.245))
print(smart_round(11.325, 2), " ", round2(11.325), " ", round_up(1.325))
print(round2(15))
# print(round2(1.325))
