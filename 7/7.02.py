# -*- encoding: utf-8 -*-
# Author: li_colin
# 词梯问题
# 构建graph

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
    for ele in g:
        print(ele)


get_graph()
