"""
Codeforces Round 244 Div 1 Problem A

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
n = int(input())
a = [int(x) for x in g()]
ct = 0
res = 0
for i in a:
    ct += i
    if ct < 0:
        res += 1
        ct = 0
print(res)