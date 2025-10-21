import sys
#sys.stdin=open("data.txt")
input=sys.stdin.readline

n,p,q,r=map(int,input().split())

a=list(map(int,input().split()))

s1=[a[i]*p for i in range(n)]

s2=[]
m=s1[0]
for i in range(n):
    m=max(m,s1[i])
    s2.append(m+a[i]*q)

s3=[]
m=s2[0]
for i in range(n):
    m=max(m,s2[i])
    s3.append(m+a[i]*r)

print(max(s3))