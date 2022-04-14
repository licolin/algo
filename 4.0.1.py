# -*- encoding: utf-8 -*-
# Author: li_colin
# 递归基础
# get_sum 求解list的和
# 进制转换 递归针对两种不同的终止条件,给出了两种不同的解法
def get_sum(ls):
    if not ls:
        return 0
    if len(ls) == 1:
        return ls[0]
    return ls[0] + get_sum(ls[1:])


# 进制转换 list解法
def list_source2base(val, base):
    digits = "0123456789ABCDEF"
    ret = []
    while val:
        ret.append(digits[val % base])
        val = val // base
    ret.reverse()
    return ''.join(ret)


# 进制转换 递归解法
def recurse_source2base(val, base):
    digits = "0123456789ABCDEF"
    if int(val) < base:
        return str(val)
    if val:
        return recurse_source2base(val // base, base) + str(digits[val % base])


# 进制转换 递归解法
def recurse_source2base1(val, base):
    digits = "0123456789ABCDEF"
    if int(val) < base:
        return str(val)
    if val:
        return recurse_source2base(val // base, base) + str(digits[val % base])


print(get_sum([1, 2, 3, 4, 5, 6]))
print(list_source2base(55, 16))
print(recurse_source2base(55, 16))
