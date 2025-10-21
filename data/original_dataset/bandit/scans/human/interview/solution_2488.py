from collections import deque
from math import ceil
 
n,d,a = map(int,input().split())
M = [list(map(int,input().split())) for i in range(n)]
M = sorted([(x,ceil(h/a)) for x,h in M])
 
que = deque()
 
ans = 0
atack = 0
for x,h in M:
  while len(que) > 0 and que[0][0] < x:
    tx,ta = que.popleft()
    atack -= ta      
  
  bomb_num = max(0, h-atack)
  atack += bomb_num
  ans += bomb_num
  
  if bomb_num > 0:
    que.append([x+d*2,bomb_num])
 
print(ans)