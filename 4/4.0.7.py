# -*- encoding: utf-8 -*-
# Author: li_colin
# 递归解决 迷宫

class Maze:
    def __init__(self, _data):
        self.maze = _data
        self.end = [1, 0]

    def isExit(self, val1, val2):
        if self.end[0] == int(val1) and self.end[1] == int(val2):
            return True

    def searchPath(self, row, col):
        if self.maze[row][col] == "+":
            return False
        if self.isExit(row, col):
            return True


_data = [
    ["+", "+", "+", "+", "+", "+", "+", "+", "+", "+"],
    [" ", " ", " ", " ", " ", "+", "+", "+", "+", "+"],
    ["+", " ", "+", " ", " ", "+", " ", "+", "+", "+"],
    ["+", " ", "+", "+", " ", " ", " ", "+", "+", "+"],
    ["+", " ", "+", "+", "+", " ", "+", "+", " ", "+"],
    ["+", " ", "+", " ", "+", " ", " ", " ", " ", "+"],
    ["+", " ", "+", " ", "+", " ", "+", " ", " ", "+"],
    ["+", " ", " ", " ", "+", " ", " ", " ", " ", "+"],
    ["+", "+", "+", "+", "+", "+", "+", "+", " ", "+"],
    ["+", "+", "+", "+", "+", "+", "+", "+", "+", "+"]
]

_maze = Maze(_data)
# for ele in _data:
#     print(" ".join(ele))
