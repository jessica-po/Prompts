import re
import itertools
from collections import Counter, deque

class Task:
    n, m = 0, 0
    graph = []
    answer = ""
	
    def getData(self):
        self.n, self.m = [int(x) for x in input().split(' ')]
        for i in range(0, self.m):
            self.graph += [[int(x) for x in input().split(' ')]]

        #inFile = open('input.txt', 'r')
        #inFile.readline().rstrip()
        #self.childs = inFile.readline().rstrip()

    def solve(self):
        graph = self.graph
        vertexDegrees = [0] * (self.n + 1)
        for edge in graph:
            vertexDegrees[edge[0]] += 1
            vertexDegrees[edge[1]] += 1
        vertexDegrees = vertexDegrees[1:]
        if vertexDegrees.count(2) == len(vertexDegrees):
            self.answer = 'ring topology'
            return
        if vertexDegrees.count(1) == 2 and vertexDegrees.count(2) == \
                len(vertexDegrees) - 2:
            self.answer = 'bus topology'
            return
        if vertexDegrees.count(1) == len(vertexDegrees) - 1:
            self.answer = 'star topology'
            return
        self.answer = 'unknown topology'

    def printAnswer(self):
        print(re.sub(r'[\[\],]', '', str(self.answer)))
        #print(self.answer[:6])
        #outFile = open('output.txt', 'w')
        #outFile.write(self.answer)

task = Task()
task.getData()
task.solve()
task.printAnswer()