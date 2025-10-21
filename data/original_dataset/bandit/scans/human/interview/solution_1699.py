"""
Codeforces Round 241 Div 1 Problem E

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
n,m = [int(x) for x in g()]

def sqr(n):
    if n == 1:
        return [1]
    if n == 2:
        return [4,3]
    if n % 2:
        return [(n+1)//2, 2] + [1] * (n-2)
    return [(n-2)//2] + [1] * (n-1)

a = sqr(n)
b = sqr(m)
for i in range(n):
    res = [str(a[i]*x) for x in b]
    print(" ".join(res))