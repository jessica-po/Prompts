"""
Codeforces Testing Round 10 Problem B

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
s = sum(a) // n
r = 0
for i in range(n-1):
    if a[i] < s:
        r += s - a[i]
        a[i+1] -= s - a[i]
    else:
        r += a[i] - s
        a[i+1] += a[i] - s
print(r)