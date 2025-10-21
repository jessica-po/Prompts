import sys
input = sys.stdin.readline # for speed up
#sys.setrecursionlimit(10**9)

n=int(input())
a=list(map(int,input().split()))

l=[0]*(n+2)
r=[0]*(n+2)
l[1]=a[0]
r[n]=a[n-1]
import math 
for ii in range(1,n):
  l[ii+1]=math.gcd(l[ii],a[ii])
  r[n-ii]=math.gcd(r[n-ii+1],a[n-1-ii])
#print(r)
#print(l)
ans=0
for ii in range(1,n+1):
  ans=max(ans,math.gcd(l[ii-1],r[ii+1]))
  #print(l[ii-1],r[ii+1])
print(ans)