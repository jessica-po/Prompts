import re
import itertools
from collections import Counter

class Task:
    strings = []
    answer = ""
	
    def getData(self):
        numberOfStrings = int(input())
        for i in range(0, numberOfStrings):
            self.strings += [input()]
	
    def solve(self):
        badStrings = set()
        for current in self.strings:
            for left in range(0, len(current)):
                for right in range(left + 1, len(current) + 1):
                    badStrings.add(current[left : right])
        alphabet = []
        for character in range(ord('a'), ord('z') + 1):
            alphabet += [chr(character)]
        
        for answerLength in range(1, 21 + 1):
            for p in itertools.product(alphabet, repeat = answerLength):
                string = re.sub("[^\w]", "", str(p));
                if string not in badStrings:
                    self.answer = string
                    return

    def printAnswer(self):
        print(self.answer)

task = Task();
task.getData();
task.solve();
task.printAnswer();