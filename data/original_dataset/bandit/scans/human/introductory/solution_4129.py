from queue import Queue
from random import shuffle
import sys
import math
import os.path


sys.setrecursionlimit(100000)

# LOG

def log(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


# INPUT

def ni():
    return map(int, input().split())


def nio(offset):
    return map(lambda x: int(x) + offset, input().split())


def nia():
    return list(map(int, input().split()))


# CONVERT
def toString(aList, sep=" "):
    return sep.join(str(x) for x in aList)


def toMapInvertIndex(aList):
    return {k: v for v, k in enumerate(aList)}


# SORT
def sortId(arr):
    return sorted(range(len(arr)), key=lambda k: arr[k])


# MAIN

n,m,s = ni()

s -= 1

adj = [[] for _ in range(n)]

for i in range(m):
    u,v = nio(-1)
    if (v != s):
        adj[u].append(v)

stack = []

visited= [False]*n

def dfs(x):
    nonlocal visited
    nonlocal stack
    visited[x] = True
    for y in adj[x]:
        if not visited[y]:
            dfs(y)

    stack.append(x)


for i in range(n):
    if not visited[i]:
        dfs(i)

# log(adj)
# log(visited)
# log(stack)

count = -1

def loang(x):
    nonlocal visited
    visited[x] = False
    for y in adj[x]:
        if visited[y]:
            loang(y)


for x in stack[::-1]:
    if visited[x]:
        count += 1
        loang(x)

print(count)