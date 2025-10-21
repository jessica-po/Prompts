import sys
input = sys.stdin.readline

n=int(input())
A=list(map(int,input().split()))

B=[(a,ind) for ind,a in enumerate(A)]
B.sort()
    
DP=[0]*(n+1)

for i in range(3,n-2):
    DP[i]=max(DP[i-1],DP[i-3]+B[i][0]-B[i-1][0])

#print(DP)

MAX=max(DP)

x=DP.index(MAX)

REMLIST=[]

while x>0:
    if DP[x]==DP[x-1]:
        x-=1
    else:
        REMLIST.append(x)
        x-=3

REMLIST.sort()
REMLIST.append(1<<60)

print(max(A)-min(A)-MAX,len(REMLIST))

ANS=[-1]*n
remind=0
NOW=1

for i in range(n):
    if i==REMLIST[remind]:
        NOW+=1
        remind+=1
    ANS[B[i][1]]=NOW
print(*ANS)