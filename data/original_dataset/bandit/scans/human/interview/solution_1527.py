from collections import deque
from copy import deepcopy

h,w = map(int,input().split())
s = [list(input()) for i in range(h)]
t = ((0,1),(1,0),(-1,0),(0,-1))
m = 0
for sy in range(h):
    for sx in range(w):
        if s[sy][sx] == "#":
            continue
        ss = deepcopy(s)
        ss[sy][sx] = "#"
        q = deque([(0,sy,sx)])
        max_cost = 0
        my,mx = 0,0
        while(q):
            cost,y,x = q.popleft()
            max_cost = max(max_cost,cost)
            cost += 1
            for i,j in t:
                ny = y+i
                nx = x+j
                if 0 <= ny < h and 0 <= nx < w:
                    if ss[ny][nx] == ".":
                        q.append((cost,ny,nx))
                        ss[ny][nx] = "#"
        m = max(m,max_cost)
print(m)