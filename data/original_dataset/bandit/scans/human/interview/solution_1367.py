"""
Codeforces Testing Round 10 Problem A

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
n, = read()
a = read()
write(n*(n+1)//2 - sum(a))