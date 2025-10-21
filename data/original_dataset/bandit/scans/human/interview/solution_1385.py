import re
from collections import Counter

class Task:
	answer = []
	str = ""
	
	def getData(self):
		x = 0
		self.str = input()
	
	def solve(self):
		list = re.findall("\".*?\"|[^ ]+", self.str)
		self.answer = ["<" + x.replace("\"", "") + ">" for x in list]
	
	def printAnswer(self):
		for x in self.answer:
			print(x)

task = Task();
task.getData();
task.solve();
task.printAnswer();