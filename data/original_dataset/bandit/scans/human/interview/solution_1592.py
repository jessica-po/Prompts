import re
import itertools
from collections import Counter, deque

class Task:
    tasks = []
    answer = "" 
	
    def getData(self):
        numberOfTasks = int(input())
        for i in range(0, numberOfTasks):
            self.tasks += [[int(x) for x in input().split(' ')]]
        #inFile = open('input.txt', 'r')
        #inFile.readline().rstrip()
        #self.childs = inFile.readline().rstrip()

    def solve(self):
        queueSize, maxQueueSize = 0, 0
        time, timeOfLastMessage = 1, 1
        currentTask = 0
        while currentTask < len(self.tasks) or queueSize > 0:
            maxQueueSize = max(maxQueueSize, queueSize)
            if currentTask < len(self.tasks):
                timeDelta = self.tasks[currentTask][0] - time
                queueSize -= min(queueSize, timeDelta)
                time += timeDelta
            else:
                timeOfLastMessage = time + queueSize
                break
                
            if currentTask < len(self.tasks) and \
                    self.tasks[currentTask][0] == time:
                queueSize += self.tasks[currentTask][1]
                currentTask += 1
        self.answer = str(timeOfLastMessage) + " " + str(maxQueueSize)

    def printAnswer(self):
        print(self.answer)
        #outFile = open('output.txt', 'w')
        #outFile.write(self.answer)

task = Task()
task.getData()
task.solve()
task.printAnswer()