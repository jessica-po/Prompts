"""
Codeforces Contest 291 Div 2 Problem B

Author  : chaotic_iak
Language: Python 3.4.2
"""

################################################### SOLUTION

def gcd(a,b):
    if a < 0: a = -a
    if b < 0: b = -b
    if a == 0: return b
    if b == 0: return a
    return gcd(b, a%b)

def main():
    n, x0, y0 = read()
    lines = set()
    for i in range(n):
        x, y = read()
        x -= x0
        y -= y0
        if x < 0 or (x == 0 and y < 0): x,y = -x,-y
        g = gcd(x,y)
        x //= g
        y //= g
        lines.add((x,y))
    return len(lines)



#################################################### HELPERS



def read(mode=2):
    # 0: String
    # 1: List of strings
    # 2: List of integers
    inputs = input().strip()
    if mode == 0: return inputs
    if mode == 1: return inputs.split()
    if mode == 2: return list(map(int, inputs.split()))

def write(s="\n"):
    if s is None: s = ""
    if isinstance(s, list): s = " ".join(map(str, s))
    s = str(s)
    print(s, end="")

write(main())