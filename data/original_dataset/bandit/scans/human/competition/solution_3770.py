import sys
input = sys.stdin.readline

N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

# node : 0<=i<=3*N-1, i:minus i+1: delete i+2: plus
# start : 3*N
# goal : 3*N+1

EDGE=[dict() for i in range(3*N+2)]
V=3*N+2
start=3*N
goal=3*N+1

for i in range(N):
    EDGE[start][3*i] = -B[i] + (1<<30)
    EDGE[3*i][3*i+1] = A[i] + (1<<30)
    EDGE[3*i+1][3*i+2] = B[i] + (1<<30)
    EDGE[3*i+2][goal] = float("inf")

for i in range(M):
    x,y=map(int,input().split())
    x-=1
    y-=1

    EDGE[3*x+1][3*y] = float("inf")
    EDGE[3*y+1][3*x] = float("inf")

ANS=0
while True:
    USED=[0]*V
    ROUTE=[-1]*V
    Q=[(start,float("inf"))]
    
    while Q: # DFS
        NOW,cost=Q.pop()
        if NOW==goal:
            break

        for to in EDGE[NOW]:
            if USED[to]==0 and EDGE[NOW][to]!=0: 
                ROUTE[to]=NOW
                USED[to]=1
                Q.append((to,min(cost,EDGE[NOW][to])))
    else:
        break
    
    ANS+=cost
    i=goal
    while i!=start: # goalからたどり,Routeを使ってEDGEの更新
        j=ROUTE[i]
        EDGE[j][i]-=cost # 使ったルートをいけなく更新
        if j in EDGE[i]:
            EDGE[i][j]+=cost # 逆向きに進めるようにする.これらを重みつきにすれ普通のフロー
        else:
            EDGE[i][j]=cost
            
        i=j
        
print(-(ANS-(N<<30)))