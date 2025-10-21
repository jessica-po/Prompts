"""
Codeforces Round 244 Div 1 Problem B

Author  : chaotic_iak
Language: Python 3.3.4
"""

class InputHandlerObject(object):
    inputs = []

    def getInput(self, n = 0):
        res = ""
        inputs = self.inputs
        if not inputs: inputs.extend(input().split(" "))
        if n == 0:
            res = inputs[:]
            inputs[:] = []
        while n > len(inputs):
            inputs.extend(input().split(" "))
        if n > 0:
            res = inputs[:n]
            inputs[:n] = []
        return res
InputHandler = InputHandlerObject()
g = InputHandler.getInput

############################## SOLUTION ##############################
n,t,c = [int(x) for x in g()]
a = [False if int(x) > t else True for x in g()]
ct = 0
res = 0
for i in a:
    if i:
        ct += 1
        if ct >= c: res += 1
    else:
        ct = 0
print(res)