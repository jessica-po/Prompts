import sys
import copy
input = sys.stdin.readline

n,m,k=list(map(int,input().split()))
A=list(map(int,input().split()))
SHOP=[list(map(int,input().split())) for i in range(m)]

A=sorted(A)[:k]
A=A[::-1]

SHOP.sort(key=lambda x:x[0])

from itertools import accumulate 

DP=[0]+list(accumulate(A))
SUM=copy.deepcopy(DP)

for i in range(k+1):
    for x,y in SHOP:
        if x>i:
            break
        DP[i]=min(DP[i],DP[i-x]+SUM[i]-SUM[i-x]-SUM[i]+SUM[i-y],DP[i-1]+A[i-1])

print(DP[-1])