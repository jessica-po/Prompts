"""
Codeforces Round 250 Div 2 Problem C

Author  : chaotic_iak
Language: Python 3.3.4
"""

class IOHandlerObject(object):
    def getInput(self, mode=2):
        # 0: String
        # 1: List of strings
        # 2: List of integers
        inputs = input().strip()
        if mode == 0:
            return inputs
        if mode == 1:
            return inputs.split()
        if mode == 2:
            return [int(x) for x in inputs.split()]

    def writeOutput(self, s="\n"):
        if isinstance(s, list): s = " ".join(s)
        print(s)

IOHandler = IOHandlerObject()
g = IOHandler.getInput
w = IOHandler.writeOutput

############################## SOLUTION ##############################
n,m = g()
v = g()
sm = 0
for i in range(m):
    x,y = g()
    sm += min(v[x-1], v[y-1])
print(sm)