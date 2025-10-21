"""
Codeforces Contest 281 Div 2 Problem B

Author  : chaotic_iak
Language: Python 3.3.4
"""

def main():
    n, = read()
    a = []
    b = []
    last = 0
    for i in range(n):
        x, = read()
        if x < 0:
            b.append(-x)
            last = 1
        else:
            a.append(x)
            last = 0
    if sum(a) > sum(b):
        print("first")
    elif sum(b) > sum(a):
        print("second")
    elif a > b:
        print("first")
    elif b > a:
        print("second")
    else:
        print("second" if last else "first")

################################### NON-SOLUTION STUFF BELOW

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