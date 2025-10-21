3

import copy


def rotate90(n, f):
    return [[f[n - j - 1][i] for j in range(n)] for i in range(n)]

def fliphor(n, f):
    return [[f[i][n - j - 1] for j in range(n)] for i in range(n)]

def flipver(n, f):
    return [[f[n - i - 1][j] for j in range(n)] for i in range(n)]

def eq(n, f, g):
    for i in range(n):
        for j in range(n):
            if f[i][j] != g[i][j]:
                return False
    return True


n = int(input())
f = [list(input()) for i in range(n)]
g = [list(input()) for i in range(n)]

for doflipv in range(2):
    for dofliph in range(2):
        for nrot in range(4):
            h = copy.deepcopy(f)
            if dofliph == 1:
                h = fliphor(n, h)
            if doflipv == 1:
                h = flipver(n, h)
            for i in range(nrot):
                h = rotate90(n, h)
            if eq(n, h, g):
                print("Yes")
                return

print("No")