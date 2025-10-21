n=int(input())
a=tuple(map(int,input().split()))
c={}
p={}
s=x=y=0
m=-1e18
for i in range(0,len(a)):
    d=c.get(a[i])
    if d!=None and s-d+a[i]*2>m:
        m=s-d+a[i]*2
        x,y=p.get(a[i]),i
    if(a[i]>0):s+=a[i]  
    if p.get(a[i])==None:
        p[a[i]]=i
        c[a[i]]=s
a=[str(i+1) for i in range(0,len(a)) if i!=x and i!=y and (a[i]<0 or i<x or i>y)]
print(m,len(a))
print(" ".join(a))