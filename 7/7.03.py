# -*- encoding: utf-8 -*-
# Author: li_colin
# 骑士问题
# 在8*8的棋盘格子里,马走日,找到一条路径使得马能走到每个格子且每个各自只走一次


class Vertex:
    def __init__(self, key):
        self.key = key
        self.connects = {}
        self.pre = None
        self.dist = sys.maxsize
        self.color = "white"

    def addNbr(self, nbr, weight):
        self.connects[nbr] = weight

    def __str__(self):
        return str(self.key) + ":" + str([i.key for i in self.connects.keys() if i is not None])

    def getWeight(self, key):
        return self.connects[key]

    def getDistance(self):
        return self.dist

    def setDistance(self, val):
        self.dist = val

    def getConnects(self):
        return self.connects

    def setPre(self, p):
        self.pre = p

    def getPre(self):
        return self.pre

    def setColor(self, color):
        self.color = color


class Graph:
    def __init__(self):
        self.vertexList = {}
        self.num = 0

    def addVertex(self, v):
        new_vertex = Vertex(v)
        self.vertexList[v] = Vertex(v)
        self.num = self.num + 1
        return new_vertex

    def getVertex(self, key):
        if key in self.vertexList:
            return self.vertexList[key]
        else:
            return None

    def addEdge(self, f, t, val=0):
        if f not in self.vertexList:
            self.addVertex(f)
        if t not in self.vertexList:
            self.addVertex(t)
        self.vertexList[f].addNbr(self.vertexList[t], val)

    def __iter__(self):
        return iter(self.vertexList.values())

    def __contains__(self, key):
        return key in self.vertexList


def gen_step(x, y, body_size):
    steps = []
    move_step = [(-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2)]
    for ele in move_step:
        new_x = x + ele[0]
        new_y = y + ele[1]
        if legalOrNot(new_x, body_size) and legalOrNot(new_y, body_size):
            steps.append((new_x, new_y))
    return steps


def legalOrNot(x, body_size):
    if 0 <= x < body_size:
        return True
    else:
        return False


def getId(col, row, body_size):
    return row * body_size + col


def genKnightGraph(body_size):
    kg = Graph()
    for col in range(body_size):
        for row in range(body_size):
            current = getId(col, row, body_size)
            child_nodes = gen_step(col, row, body_size)
            for ele in child_nodes:
                child_node_id = getId(ele[0], ele[1], body_size)
                kg.addEdge(current, child_node_id)
    return kg
