import sys
input = sys.stdin.readline

n,m,k=list(map(int,input().split()))
EDGE=[list(map(int,input().split())) for i in range(m)]

EDGE.sort(key=lambda x:x[2])
EDGE=EDGE[:k]

COST_vertex=[[] for i in range(n+1)]
for a,b,c in EDGE:
    COST_vertex[a].append((b,c))
    COST_vertex[b].append((a,c))

for i in range(min(m,k)):
    x,y,c=EDGE[i]
    EDGE[i]=(c,x,y)


USED_SET=set()

ANS=[-1<<50]*k

import heapq

while EDGE:
    c,x,y = heapq.heappop(EDGE)

    if (x,y) in  USED_SET or c>=-ANS[0]:
        continue

    else:
        heapq.heappop(ANS)
        heapq.heappush(ANS,-c)
        USED_SET.add((x,y))
        USED_SET.add((y,x))

    for to,cost in COST_vertex[x]:
        if to!=y and not((y,to) in USED_SET) and c+cost<-ANS[0]:
            heapq.heappush(EDGE,(c+cost,y,to))
            #USED_SET.add((y,to))
            #USED_SET.add((to,y))

    for to,cost in COST_vertex[y]:
        if to!=x and not((x,to) in USED_SET) and c+cost<-ANS[0]:
            heapq.heappush(EDGE,(c+cost,x,to))
            #USED_SET.add((x,to))
            #USED_SET.add((to,x))

print(-ANS[0])