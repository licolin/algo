# -*- encoding: utf-8 -*-
# Author: li_colin
# 递归 解决hanoi 塔


def move_pie(_from, to, height):
    print(f"from {_from} to {to} move id is {height}")


def move_tower(_from, _with, _to, height):
    if height >= 1:
        move_tower(_from, _to, _with, height - 1)
        move_pie(_from, _to, height)
        move_tower(_with, _from, _to, height - 1)


move_tower("#1", "#2", "#3", 2)
