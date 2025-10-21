import sys
#sys.stdin=open("data.txt")
input=sys.stdin.readline

n,m=map(int,input().split())

l=list(map(int,input().split()))
for i in range(len(l)):
    l[i]-=1

use=[0]*n
a=[0]*n
bad=0

for i in range(len(l)-1):
    # transfer l[i] to l[i+1]
    if a[l[i]] and a[l[i]]%n!=(l[i+1]-l[i])%n:
        bad=1
        break
    use[(l[i+1]-l[i])%n]=1
    a[l[i]]=(l[i+1]-l[i])%n
    if a[l[i]]==0: a[l[i]]=n

if not bad:
    # fill in gaps
    for i in range(n):
        if a[i]==0:
            for j in range(1,n+1):
                if not use[j%n]:
                    a[i]=j
                    use[j%n]=1
                    break
    if sum(use)==n:
        print(" ".join(map(str,a)))
    else:
        print("-1")
else:
    print("-1")