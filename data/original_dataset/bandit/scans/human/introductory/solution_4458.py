n=int(input())
p=list(map(int,input().split()))

c=1

q=p[0]

for i in range(1,n):
    q=min(q,p[i])
    if p[i]<=q:
        c+=1

print(c)