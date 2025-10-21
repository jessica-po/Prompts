"""
Codeforces Contest 261 Div 2 Problem B

Author  : chaotic_iak
Language: Python 3.3.4
"""

def main():
    n, = read()
    a = read()
    mn = 10**9+1
    mncount = 0
    mx = 0
    mxcount = 0
    for i in range(n):
        if a[i] < mn:
            mn = a[i]
            mncount = 1
        elif a[i] == mn:
            mncount += 1
        if a[i] > mx:
            mx = a[i]
            mxcount = 1
        elif a[i] == mx:
            mxcount += 1
    if mx != mn:
        print(mx-mn, mncount*mxcount)
    else:
        print(0, n*(n-1)//2)

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