import sys
#sys.stdin=open("data.txt")
input=sys.stdin.readline

d={}

n=int(input())
for _ in range(n):
    i,j=map(int,input().split())
    d[i]=j
m=int(input())
for _ in range(m):
    i,j=map(int,input().split())
    if i in d and d[i]>j: continue
    d[i]=j

ans=0
for i,j in d.items():
    ans+=j
print(ans)