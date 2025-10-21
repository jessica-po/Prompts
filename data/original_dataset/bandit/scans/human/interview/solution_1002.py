"""
Codeforces Round 251 Div 2 Problem A

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
n,d = read()
t = read()
s = sum(t) + 10*n - 10
if s > d:
    print(-1)
else:
    print((d-sum(t))//5)