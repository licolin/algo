# -*- encoding: utf-8 -*-
# Author: li_colin
# 词梯问题
# 构建graph
import sys


class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, val):
        self.data.insert(0, val)

    def dequeue(self):
        return self.data.pop()

    def size(self):
        return len(self.data)


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


def get_graph():
    g = Graph()
    f = open("rawwords.txt", 'r')
    bucket = {}
    for ele in f:
        word = ele[:4]
        for i in range(4):
            key = word[0:i] + "_" + word[i + 1:]
            if key not in bucket:
                bucket[key] = [word]
            else:
                if word not in bucket[key]:
                    bucket[key].append(word)
                else:
                    pass
    f.close()
    for key in bucket:
        for word1 in bucket[key]:
            for word2 in bucket[key]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g


def travel(vertex):
    x = vertex
    while x is not None:
        print(x.key)
        x = x.getPre()


gh = get_graph()


def bfs(start):
    start.setDistance = 0
    start.setPre = None
    _vertexQueue = Queue()
    _vertexQueue.enqueue(start)
    while _vertexQueue.size() > 0:
        _new_vertex = _vertexQueue.dequeue()
        for ele in _new_vertex.getConnects():
            if ele.color == "white":
                _vertexQueue.enqueue(ele)
                ele.setColor("black")
                ele.setDistance(_new_vertex.getDistance() + 1)
                ele.setPre(_new_vertex)
        _new_vertex.setColor("black")


bfs(gh.getVertex("FOOL"))
travel(gh.getVertex("SAGE"))
