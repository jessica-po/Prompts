from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

H,W = inpl()
rr = inpl()
cc = inpl()

MAP = [[-1]*W for _ in range(H)]

for x,c in enumerate(cc):
    for y in range(c):
        MAP[y][x] = 1
    if c < H:
        MAP[c][x] = 0


for y,r in enumerate(rr):
    for x in range(r):
        if MAP[y][x] == 0:
            print(0)
            return
        MAP[y][x] = 1
    if r < W:
        if MAP[y][r] == 1:
            print(0)
            return
        MAP[y][r] = 0

cnt = 0
for y in range(H):
    for x in range(W):
        if MAP[y][x] == -1:
            cnt += 1

print(pow(2,cnt,mod))