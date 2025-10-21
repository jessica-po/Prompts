import sys
input = sys.stdin.readline

n,x=list(map(int,input().split()))
A=list(map(int,input().split()))

MIN_R=[A[-1]]
for a in A[:-1][::-1]:
    MIN_R.append(min(a,MIN_R[-1]))

MIN_R=MIN_R[::-1]

MAX=x

for i in range(n-1):
    if A[i]>MIN_R[i+1]:
        MAX=min(MAX,A[i])

MAX_L=[A[0]]
for a in A[1:]:
    MAX_L.append(max(a,MAX_L[-1]))

MIN=0
for i in range(1,n):
    if MAX_L[i-1]>A[i]:
        MIN=max(MIN,A[i])

NEED=[i for i in range(x+3)]

for i in range(n-1):
    if A[i]>MIN_R[i+1]:
        NEED[1]=max(NEED[1],MIN_R[i+1])
        NEED[MIN_R[i+1]+1]=max(NEED[MIN_R[i+1]+1],A[i])

for i in range(1,x+2):
    NEED[i]=max(NEED[i],NEED[i-1])

ANS=0

for i in range(1,MAX+1):
    ANS+=x-max(MIN,NEED[i])+1

    #print(i,ANS)

print(ANS)