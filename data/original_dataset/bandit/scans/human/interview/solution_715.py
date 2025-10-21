"""
Codeforces Round 250 Div 2 Problem A

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
a,b,c,d = g(0),g(0),g(0),g(0)
r = [(len(a)-2,0), (len(b)-2,1), (len(c)-2,2), (len(d)-2,3)]
r.sort()
t = -1
if r[0][0]*2 <= r[1][0]: t = r[0][1]
if r[3][0] >= r[2][0] * 2:
    if not t+1:
        t = r[3][1]
    else:
        t = 5

if t == -1 or t == 5:
    print("C")
else:
    print(chr(65+t))