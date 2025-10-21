"""
Codeforces Testing Round 10 Problem C

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
def g(n):
    return (10**n-1)//9

def solve(n):
    if n <= 6: return n
    if 7 <= n <= 11: return 13-n
    l = 1
    while g(l) < n: l += 1
    l -= 1
    gl = g(l)
    a = n
    res1 = 0
    res1 += (a // gl) * l
    a %= gl
    res1 += solve(a)
    b = g(l+1) - n
    res2 = l+1
    res2 += (b // gl) * l
    b %= gl
    res2 += solve(b)
    return min(res1, res2)

n, = read()
print(solve(n))