import sys
n,m=list(map(int,sys.stdin.readline().split()))
P={}
for i in range(m):
    a,b=list(map(int,sys.stdin.readline().split()))
    P[(a-1,b-1)]=1

A=[-1]*n
A[0]=0
for i in range(1,n):
    j=1
    A[i]=i
    x=i
    while(x>0 and (A[x-1],A[x]) in P):
        A[x-1],A[x]=A[x],A[x-1]
        x-=1
Anss=""
for i in range(n):
    Anss+=str(A[i]+1)+" "
sys.stdout.write(Anss)