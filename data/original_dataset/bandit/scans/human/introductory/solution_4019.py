import sys
input = sys.stdin.readline

n,m,D=list(map(int,input().split()))
E=[list(map(int,input().split())) for i in range(m)]


EDGELIST=[[] for i in range(n+1)]

for x,y in E:
    EDGELIST[x].append(y)
    EDGELIST[y].append(x)

Group=[i for i in range(n+1)]

def find(x):
    while Group[x] != x:
        x=Group[x]
    return x

def Union(x,y):
    if find(x) != find(y):
        Group[find(y)]=Group[find(x)]=min(find(y),find(x))

ONE=EDGELIST[1]

for x,y in E:
    if x==1 or y==1:
        continue
    Union(x,y)

ONEU=[find(e) for e in ONE]

if len(set(ONEU))>D or D>len(ONE):
    print("NO")
    return
else:
    print("YES")

USED=set()
ANS=[]
from collections import deque
QUE=deque()
check=[0]*(n+1)
check[1]=1

for j in range(len(ONE)):
    if find(ONE[j]) in USED:
        continue
    else:
        ANS.append([1,ONE[j]])
        QUE.append(ONE[j])
        USED.add(find(ONE[j]))
        check[ONE[j]]=1
        D-=1

j=0
for i in range(D):
    while check[ONE[j]]==1:
        j+=1
    ANS.append([1,ONE[j]])
    QUE.append(ONE[j])
    check[ONE[j]]=1
    

while QUE:
    x=QUE.popleft()
    check[x]=1

    for to in EDGELIST[x]:
        if check[to]==0:
            ANS.append([x,to])
            QUE.append(to)
            check[to]=1
        
#print(ANS)
for x,y in ANS:
    print(x,y)