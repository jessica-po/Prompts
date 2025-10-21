# cook your dish here
import copy
import bisect
n,q=list(map(int,input().split()))

a=list(map(int,input().split()))

a.sort()
b=copy.copy(a)
for i in range(1,len(b)):
 b[i]+=b[i-1]
##print(b)
for i in range(q):
 x=int(input())
 ans=bisect.bisect_left(a,x*2)
 if ans==0:
  ans1=b[n-1]
 else:
  ans1=b[n-1]-b[ans-1]
 print(ans1)