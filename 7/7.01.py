# -*- encoding: utf-8 -*-
# Author: li_colin
# graph

class Vertex:
    def __init__(self, key):
        self.key = key
        self.connects = {}

    def addNbr(self, nbr, weight):
        self.connects[nbr] = weight

    def __str__(self):
        return str(self.key) + ":" + str([i.key for i in self.connects.keys() if i is not None])

    def getWeight(self, key):
        return self.connects[key]


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

    def addWeight(self, f, t, val=0):
        if f not in self.vertexList:
            self.addVertex(f)
        if t not in self.vertexList:
            self.addVertex(t)
        self.vertexList[f].addNbr(self.vertexList[t], val)

    def __iter__(self):
        return iter(self.vertexList.values())

    def __contains__(self, key):
        return key in self.vertexList


g = Graph()
g.addVertex("v0")
g.addWeight("v0", "v1", 5)
g.addWeight("v0", "v2", 3)
g.addWeight("v1", "v2", 6)
for ele in g:
    print(ele)
