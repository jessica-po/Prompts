import re
import itertools
from collections import Counter, deque

class Task:
    a = []
    d = 0
    answer = 0
	
    def getData(self):
        n, m, self.d = [int(x) for x in input().split(' ')]
        for _ in range(n):
            self.a += [int(x) for x in input().split(' ')]
        #inFile = open('input.txt', 'r')
        #inFile.readline().rstrip()
        #self.childs = inFile.readline().rstrip()

    def solve(self):
        a = self.a

        for x in a:
            if x % self.d != a[0] % self.d:
                self.answer = -1
                return
        
        a = [x // self.d for x in a]
        a.sort()
        
        d = [sum(a)] + [0 for _ in range(1, a[-1] + 1)]
        
        lessCurrentLevel = 0
        counter = Counter(a)
        
        for level in range(1, a[-1] + 1):
            lessCurrentLevel += counter[level - 1]
            d[level] = d[level - 1] + lessCurrentLevel - \
                    (len(a) - lessCurrentLevel)
        self.answer = min(d)

    def solve2(self):
        a, d = self.a, self.d
        for i in range(1, len(a)):
            if a[i] % d != a[0] % d:
                self.answer = -1
                return
        a = [x // d for x in a]
        d = [abs(a[0] - i) for i in range(10000 + 1)]
        for i in range(1, len(a)):
            for j in range(0, len(d)):
                d[j] += abs(a[i] - j)
        self.answer = min(d)

    def printAnswer(self):
        print(self.answer)
        #print(re.sub('[\[\],]', '', str(self.answer)))
        #outFile = open('output.txt', 'w')
        #outFile.write(self.answer)

task = Task()
task.getData()
task.solve()
task.printAnswer()