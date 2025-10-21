import sys
#sys.stdin=open("data.txt")
input=sys.stdin.readline

n,m=list(map(int,input().split()))

possible1=[set() for _ in range(200)]
possible2=[set() for _ in range(200)]
weird=[0]*15

p1=list(map(int,input().split()))
p2=list(map(int,input().split()))

for i in range(n):
    for j in range(m):
        a=sorted(p1[i*2:i*2+2])
        b=sorted(p2[j*2:j*2+2])
        if a==b: continue
        got=-1
        if a[0] in b: got=a[0]
        if a[1] in b: got=a[1]
        if got==-1: continue
        weird[got]=1
        possible1[a[0]*11+a[1]].add(got)
        possible2[b[0]*11+b[1]].add(got)

if sum(weird)==1:
    print(weird.index(1))
elif max(len(i) for i in possible1)==1 and max(len(i) for i in possible2)==1:
    print(0)
else:
    print(-1)