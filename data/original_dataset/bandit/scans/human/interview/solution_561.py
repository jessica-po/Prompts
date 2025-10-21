n=int(input())
a=list(map(int,input().split()))
if n==1:
    print(-1)
    return
a.sort()
d=[]
for i in range(1,n):
    d.append(a[i]-a[i-1])
if min(d)==max(d)==0:
    print(1)
    print(a[0])
elif n==2:
    if d[0]%2:
        print(2)
        print(a[0]-d[0],a[1]+d[0])
    else:
        print(3)
        print(a[0]-d[0],a[0]+d[0]//2,a[1]+d[0])
elif min(d)==max(d):
    print(2)
    print(a[0]-d[0],a[-1]+d[0])
else:
    m1=0
    m2=0
    for i in range(1,n-1):
        if d[i]<d[m1]: m1=i
        if d[i]>d[m2]: m2=i
    c=d.count(d[m1])
    if c==n-2 and d[m1]*2==d[m2]:
        print(1)
        print(a[m2]+d[m1])
    else:
        print(0)