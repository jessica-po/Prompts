import re
import itertools
from collections import Counter

class Task:
    a = []
    answer = []
	
    def getData(self):
        input()
        self.a = [int(x) for x in input().split(" ")]
	
    def solve(self):
        currentFolderCounter = 0
        badDaysCounter = 0
        for x in self.a:
            if x >= 0:
                currentFolderCounter += 1
            elif badDaysCounter <= 1:
                currentFolderCounter += 1
                badDaysCounter += 1
            else:
                self.answer += [currentFolderCounter]
                currentFolderCounter = 1
                badDaysCounter = 1
        if currentFolderCounter > 0:
            self.answer += [currentFolderCounter]

    def printAnswer(self):
        print(len(self.answer))
        print(re.sub('[\[\],]', '', str(self.answer)))

task = Task();
task.getData();
task.solve();
task.printAnswer();