import sys
from collections import deque

def solve():
    xadj, yadj = [0, 0, - 1, 1, -1, -1, 1, 1], [1, -1, 0, 0, -1, 1, -1, 1]
    x0, y0, x1, y1, = rv()
    n, = rv()
    good = set()
    visited = dict()
    for seg in range(n):
        r, a, b, = rv()
        for c in range(a, b + 1): good.add((r, c))
    points = deque()
    points.append((x0, y0, 0))
    visited[(x0, y0)] = 0
    while len(points) > 0:
        cur = points.popleft()
        for i in range(8):
            pos = (cur[0] + xadj[i], cur[1] + yadj[i])
            if pos in good and pos not in visited:
                points.append((pos[0], pos[1], cur[2] + 1))
                visited[pos] = cur[2] + 1
    print(visited[(x1, y1)] if (x1, y1) in visited else - 1)







def prt(l): return print(''.join(l))
def rv(): return map(int, input().split())
def rl(n): return [list(map(int, input().split())) for _ in range(n)]
if sys.hexversion == 50594544 : sys.stdin = open("test.txt")
solve()