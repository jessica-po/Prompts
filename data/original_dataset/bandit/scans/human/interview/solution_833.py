"""
Codeforces Round 252 Div 2 Problem B

Author  : chaotic_iak
Language: Python 3.3.4
"""

def read(mode=2):
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

def write(s="\n"):
    if isinstance(s, list): s = " ".join(s)
    s = str(s)
    print(s, end="")

################################################### SOLUTION
n,v = read()
a = []
for i in range(n):
    a.append(read())
a.sort(key=lambda x: x[0])
res = 0
for day in range(1, 3002):
    n = 0
    while a and a[0][0] <= day:
        if a[0][1] <= v-n:
            n += a[0][1]
            a[0][1] = 0
        else:
            a[0][1] -= v-n
            n = v
        if a[0][1] == 0:
            a.pop(0)
        else:
            break
    while a and a[0][0] == day-1: a.pop(0)
    res += n
print(res)