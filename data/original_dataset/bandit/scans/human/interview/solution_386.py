"""
Codeforces Round 241 Div 1 Problem A

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
n = int(input().strip())
mn = -2*10**9
mx = 2*10**9
repl = [(">", "<="), (">=", "<"), ("<=", ">"), ("<", ">=")]
for i in range(n):
    a = g()
    a[1] = int(a[1])
    if a[2] == "N":
        for qq,qqq in repl:
            if qq == a[0]:
                a[0] = qqq
                break
    if a[0] == ">": a[1] += 1
    if a[0] == "<": a[1] -= 1
    if a[0][0] == ">": mn = max(mn, a[1])
    if a[0][0] == "<": mx = min(mx, a[1])

if mn <= mx:
    print(mn)
else:
    print("Impossible")