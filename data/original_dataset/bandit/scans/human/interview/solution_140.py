import sys
input = sys.stdin.readline

n,m=list(map(int,input().split()))

A=[]
COVERED=[0]*(m+1)

for i in range(n):
    x,y=list(map(int,input().split()))
    A.append((x-y,x+y))

    for j in range(max(0,x-y),min(m+1,x+y+1)):
        COVERED[j]=1

if min(COVERED[1:])==1:
    print(0)
    return

A.sort()

DP=[m]*(m+2)
DP[1]=0

covind=1

while COVERED[covind]==1:
    DP[covind]=0
    covind+=1
DP[covind]=0

NEXT=[i+1 for i in range(m+1)]
for j in range(m-1,-1,-1):
    if COVERED[j+1]==1:
        NEXT[j]=NEXT[j+1]

def nex(i):
    if i<=m:
        return NEXT[i]
    else:
        return m+1


for i in range(1,m+1):
    if COVERED[i]==1:
        continue

    for x,y in A:
        if x<i:
            continue
        DP[nex(y+(x-i))]=min(DP[i]+(x-i),DP[nex(y+(x-i))])

#print(DP)
ANS=DP[-1]
for i in range(m,-1,-1):
    if DP[i]!=m+1:
        ANS=(min(ANS,DP[i]+(m+1-i)))

print(ANS)