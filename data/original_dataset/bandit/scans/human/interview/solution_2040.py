"""
Codeforces Contest 289 Div 2 Problem C

Author  : chaotic_iak
Language: Python 3.4.2
"""

################################################### SOLUTION

def printing(num):
    arr = num[:]
    while len(arr) > 1 and arr[-1] == 0: arr.pop()
    print("".join(map(str, reversed(arr))))

def main():
    n, = read()
    last = [0]*500
    for i in range(n):
        b, = read()
        last[0] += 1
        p = 0
        while last[p] == 10:
            last[p] = 0
            p += 1
            last[p] += 1
        p = 0
        while sum(last) > b:
            last[p] = 0
            p += 1
            k = p
            last[k] += 1
            while last[k] == 10:
                last[k] = 0
                k += 1
                last[k] += 1
        p = 0
        while sum(last) < b:
            while last[p] == 9: p += 1
            last[p] += 1
        printing(last)



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