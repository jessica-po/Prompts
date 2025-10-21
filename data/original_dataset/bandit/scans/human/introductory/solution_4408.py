from queue import Queue
import sys
import math
import os.path

# CONFIG
sys.setrecursionlimit(10**9)

# LOG
def log(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


# INPUT
def ni():
    return list(map(int, input().split()))


def nio(offset):
    return [int(x) + offset for x in input().split()]


def nia():
    return list(map(int, input().split()))


# CONVERT
def toString(aList, sep=" "):
    return sep.join(str(x) for x in aList)


def mapInvertIndex(aList):
    return {k: v for v, k in enumerate(aList)}

def countMap(arr):
    m = {}
    for x in arr:
        m[x] = m.get(x,0) + 1
    return m

def sortId(arr):
    return sorted(list(range(arr)), key=lambda k: arr[k])

# MAIN

n, k = ni()
c = nia()
f = nia()
h = [0] + (nia())

cc = countMap(c)
cf = countMap(f)

n1 = n+1
k1 = k+1

nk1 = n*k+1
dp = [[0]*nk1 for _ in range(n1)]


for ni in range(1,n1):
    for ki in range(1,nk1):
        mficount = min(k,ki) + 1        
        for kii in range(mficount):
            # log(ni,ki, kii, dp[ni][ki], dp[ni-1][ki-kii] + h[kii])
            dp[ni][ki] = max(dp[ni][ki], dp[ni-1][ki-kii] + h[kii])
    # log(dp[ni])

# log(n,k)
# log("c", cc)
# log("f", cf)
# log("h", h)
# log(dp)

res = 0


for fk,fv in list(cf.items()):
    # log(fk, fv, cc.get(fk,0))
    res += dp[fv][cc.get(fk,0)]

print(res)