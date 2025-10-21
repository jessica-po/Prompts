import sys
input = sys.stdin.readline

n=int(input())
F=list(map(int,input().split()))

USE=[0]*(n+1)

B=[]
for i in range(n):
    USE[F[i]]=1
    if F[i]==0:
        B.append(i+1)

A=[]
for i in range(1,n+1):
    if USE[i]==0:
        A.append(i)
        
for i in range(len(A)-1):
    if A[i]==B[i]:
        A[i],A[i+1]=A[i+1],A[i]

if A[-1]==B[-1]:
    A[-1],A[-2]=A[-2],A[-1]

ind=0

for i in range(n):
    if F[i]==0:
        F[i]=A[ind]
        ind+=1

print(*F)