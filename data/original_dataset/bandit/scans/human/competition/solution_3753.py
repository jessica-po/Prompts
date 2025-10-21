import sys
input = sys.stdin.readline

n,m=list(map(int,input().split()))
MAP=[list(input().strip()) for i in range(n)]

from collections import deque
Q=deque()
Q.append([0,0])

while Q:
    x,y=Q.pop()

    if x+1<n and MAP[x+1][y]==".":
        MAP[x+1][y]=1
        Q.append([x+1,y])

    if y+1<m and MAP[x][y+1]==".":
        MAP[x][y+1]=1
        Q.append([x,y+1])

Q.append([n-1,m-1])


while Q:
    x,y=Q.pop()

    if x-1>=0 and MAP[x-1][y]==1:
        MAP[x-1][y]=0
        Q.append([x-1,y])

    if y-1>=0 and MAP[x][y-1]==1:
        MAP[x][y-1]=0
        Q.append([x,y-1])

if MAP[n-1][m-1]!=1:
    print(0)
    return

SCORE=[0]*(n+m+5)

for i in range(n):
    for j in range(m):
        if MAP[i][j]==0:
            SCORE[i+j]+=1

if 1 in SCORE:
    print(1)
else:
    print(2)