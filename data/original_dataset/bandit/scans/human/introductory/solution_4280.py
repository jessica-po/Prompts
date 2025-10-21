import sys
input = sys.stdin.readline

n,k=list(map(int,input().split()))
R=[list(map(int,input().split())) for i in range(n-1)]

RDICT={tuple(sorted([R[i][0],R[i][1]])):i for i in range(n-1)}

C=[[] for i in range(n+1)]

for x,y in R:
    C[x].append(y)
    C[y].append(x)

CLEN=[]
for i in range(1,n+1):
    CLEN.append(len(C[i]))
    
from collections import Counter
counter=Counter(CLEN)

CV=sorted(list(counter.keys()),reverse=True)

cvsum=0
cities=1

for cv in CV:
    cvsum+=counter[cv]
    if cvsum>k:
        cities=cv
        break

print(cities)
ANS=[0]*(n-1)

from collections import deque
QUE = deque()
QUE.append([1,1])
VISITED=[0]*(n+1)

while QUE:
    city,roadnum=QUE.pop()
    VISITED[city]=1

    for to in C[city]:
        if VISITED[to]==0:
            ANS[RDICT[tuple(sorted([city,to]))]]=roadnum
            roadnum=roadnum%cities+1
            QUE.append([to,roadnum])

print(*ANS)