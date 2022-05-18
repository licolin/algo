# -*- encoding: utf-8 -*-
# Author: li_colin
# graph

class Vertex:
    def __init__(self, key):
        self.key = key
        self.connects = {}

    def addNbr(self, key, weight):
        self.connects[key] = weight

    def __str__(self):
        print(self.key, ":", "".join([str(i) for i in self.connects.keys()]))

    def getWeight(self, key):
        return self.connects[key]


class Graph:
    def __init__(self):
        self.vertexList = {}
        self.num = 0

    def addVertex(self, v):
        if v not in self.vertexList:
            self.vertexList[v] = Vertex(v)

    def addWeight(self, f, t, val=0):
        if f not in self.vertexList:
            self.addVertex(f)
        if t not in self.vertexList:
            self.addVertex(t)
        self.vertexList[f].addNbr(t, val)

    def __str__(self):
        for ele in self.vertexList:
            print(ele, ":",
                  "".join([" " + str(i) + "-" + str(self.vertexList[ele].connects[i]) for i in
                           self.vertexList[ele].connects.keys() if i is not None]))


g = Graph()
g.addVertex("v0")
g.addWeight("v0", "v1", 5)
g.addWeight("v0", "v2", 3)
g.addWeight("v1", "v2", 6)
print(g)
