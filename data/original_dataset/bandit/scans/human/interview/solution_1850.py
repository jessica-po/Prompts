n,p=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
r=a[p-1]+b[0]
cou=0
for i in range(p-1):
    if a[i]+b[-1]<=r:
        cou+=1;del b[-1]
print(p-cou)