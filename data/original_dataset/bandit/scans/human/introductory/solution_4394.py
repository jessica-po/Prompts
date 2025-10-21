import sys
input = sys.stdin.readline

n,m=list(map(int,input().split()))
EDGE=[list(map(int,input().split())) for i in range(m)]

EDGE.sort(key=lambda x:x[2])

WCHANGE=[]
for i in range(1,m):
    if EDGE[i-1][2]!=EDGE[i][2]:
        WCHANGE.append(i)

WCHANGE.append(m)

Group=[i for i in range(n+1)]

def find(x):
    while Group[x] != x:
        x=Group[x]
    return x

def Union(x,y):
    if find(x) != find(y):
        Group[find(y)]=Group[find(x)]=min(find(y),find(x))


NOW=0
noneed=[0]*m
ANS=0
for wc in WCHANGE:
    for j in range(NOW,wc):

        if find(EDGE[j][0])==find(EDGE[j][1]):
            noneed[j]=1

    for j in range(NOW,wc):
        if noneed[j]==1:
            continue      
        x,y,w=EDGE[j]
        if find(x)!=find(y):
            Union(x,y)
        else:
            ANS+=1

    NOW=wc

print(ANS)