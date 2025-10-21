import sys
input = sys.stdin.readline

n,m,k,q=list(map(int,input().split()))
TR=[list(map(int,input().split())) for i in range(k)]
SAFE=list(map(int,input().split()))
SAFE.sort()

TRLIST=[[] for i in range(n+1)]

for x,y in TR:
    TRLIST[x].append(y)

while TRLIST[-1]==[]:
    TRLIST.pop()
    n-=1


START={1:0} #place,step

import bisect

for step in range(1,n):
    if TRLIST[step]==[] and step!=1:
        continue
    elif TRLIST[step]==[] and step==1:
        MIN=MAX=1
    else:
        MIN=min(TRLIST[step])
        MAX=max(TRLIST[step])

    MINind=max(0,bisect.bisect_left(SAFE,MIN)-1)
    MIN_L=SAFE[MINind]
    if MINind==q-1:
        MIN_R=MIN_L
    else:
        MIN_R=SAFE[MINind+1]

    MAXind=max(0,bisect.bisect_left(SAFE,MAX)-1)
    MAX_L=SAFE[MAXind]
    if MAXind==q-1:
        MAX_R=MAX_L
    else:
        MAX_R=SAFE[MAXind+1]
    

    NEXT=dict()

    for start in START:
        st=START[start]
        
        NEXT[MIN_L]=min(st+abs(MAX-start)+abs(MAX-MIN)+abs(MIN_L-MIN),NEXT.get(MIN_L,1<<50))
        NEXT[MIN_R]=min(st+abs(MAX-start)+abs(MAX-MIN)+abs(MIN_R-MIN),NEXT.get(MIN_R,1<<50))
        NEXT[MAX_L]=min(st+abs(MIN-start)+abs(MAX-MIN)+abs(MAX_L-MAX),NEXT.get(MAX_L,1<<50))
        NEXT[MAX_R]=min(st+abs(MIN-start)+abs(MAX-MIN)+abs(MAX_R-MAX),NEXT.get(MAX_R,1<<50))

    START=NEXT
    #print(START)

LAST=1<<50

if TRLIST[n]==[]:
    print(min(START.values())+n-1)
    return

MIN=min(TRLIST[n])
MAX=max(TRLIST[n])
#print(START)
for start in START:
    st=START[start]
    
    LAST=min(LAST,st+abs(MAX-start)+abs(MAX-MIN),st+abs(MIN-start)+abs(MAX-MIN))


print(LAST+n-1)