"""
Codeforces Round 252 Div 2 Problem C

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
n,m,k = read()

cells = []
for i in range(n):
    if not i%2:
        for j in range(m): cells.append((i+1,j+1))
    else:
        for j in range(m-1, -1, -1): cells.append((i+1,j+1))

ct = 0
for i in range(k-1):
    print(2, cells[ct][0], cells[ct][1], cells[ct+1][0], cells[ct+1][1])
    ct += 2

print(len(cells) - ct, end=" ")
for i in cells[ct:]:
    print(i[0], i[1], end=" ")