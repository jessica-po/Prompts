"""
Codeforces Round 248 Div 2 Problem A

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
c100 = a.count(100)
if sum(a) % 200:
    print("NO")
elif n % 2 and not c100:
    print("NO")
else:
    print("YES")