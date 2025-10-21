import re
import itertools
from collections import Counter

class Task:
    n, m = 0, 0
    petyaScore = 0
    vasyaScore = 0
	
    def getData(self):
        self.n, self.m = [int(x) for x in input().split(" ")]
	
    def solve(self):
        n = self.n
        m = self.m

        if n != m:
            self.vasyaScore = min(n, m)
        else:
            self.vasyaScore = min(n, m)
        self.petyaScore = self.n + self.m - 1 - self.vasyaScore 

    def printAnswer(self):
        print(self.petyaScore, self.vasyaScore)

task = Task();
task.getData();
task.solve();
task.printAnswer();