import sys
#sys.stdin=open("data.txt")
input=sys.stdin.readline
mii=lambda:list(map(int,input().split()))

n=int(input())

l1=[]
l2=[]

for i in range(n):
    a,b=mii()
    if a<b:
        l1.append((-a,b,i))
    else:
        l2.append((a,b,i))

if len(l1)>len(l2):
    l1.sort()
    print(len(l1))
    print(" ".join([str(x[2]+1) for x in l1]))
else:
    l2.sort()
    print(len(l2))
    print(" ".join([str(x[2]+1) for x in l2]))