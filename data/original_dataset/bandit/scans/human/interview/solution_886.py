"""
Codeforces Contest 288 Div 2 Problem B

Author  : chaotic_iak
Language: Python 3.4.2
"""

################################################### SOLUTION

def main():
    n = read(0)
    ld = int(n[-1])
    last = -1
    for i in range(len(n)-1):
        c = int(n[i])
        if c%2 == 0 and c < ld:
            return n[:i] + n[-1] + n[i+1:-1] + n[i]
        if c%2 == 0:
            last = i
    if last == -1:
        return -1
    return n[:last] + n[-1] + n[last+1:-1] + n[last]



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