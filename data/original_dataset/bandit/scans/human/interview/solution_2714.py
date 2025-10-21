mod=998244353
import sys
input = sys.stdin.readline
from collections import deque
from collections import Counter


def calc(s,a):
    return (pow(2,s,mod)+pow(2,a-s,mod))%mod

 
def find(x):
    while Group[x] != x:
        x=Group[x]
    return x

def Union(x,y):
    if find(x) != find(y):
        Group[find(y)]=Group[find(x)]=min(find(y),find(x))



testcase=int(input())
for test in range(testcase):
    n,m=list(map(int,input().split()))
    EDGE=[list(map(int,input().split())) for i in range(m)]
    EDGELIST=[[] for j in range(n+1)]
    ANS=1


    Group=[j for j in range(n+1)]

    for a,b in EDGE:
        Union(a,b)
        EDGELIST[a].append(b)
        EDGELIST[b].append(a)

    testing=[None]*(n+1)
    flag=1

    for i in range(1,n+1):
        if testing[i]!=None:
            continue

        score=1
        allscore=1

        testing[i]=1
        QUE = deque([i])
        while QUE:
            x=QUE.pop()
            for to in EDGELIST[x]:
                if testing[to]==-testing[x]:
                    continue
                if testing[to]==testing[x]:
                    flag=0
                    break
                testing[to]=-testing[x]
                if testing[to]==1:
                    score+=1
                allscore+=1
                QUE.append(to)
                
            if flag==0:
                break
        if flag==0:
            break
        #print(score,allscore)
        ANS=ANS*calc(score,allscore)%mod
    if flag==0:
        print(0)
        continue

    print(ANS)