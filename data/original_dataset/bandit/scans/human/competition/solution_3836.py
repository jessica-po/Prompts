n=int(input())
a=[];b=[];c=[];d=[]
for i in range(n):
    opt,num=[int(x) for x in input().split()]
    if opt==0:
        a.append(num)
    if opt==10:
        b.append(num)
    if opt==1:
        c.append(num)
    if opt==11:
        d.append(num)
ans=0
ans+=sum(d)
b.sort(reverse=True)
c.sort(reverse=True)
if len(b)<len(c):
    ans+=sum(b)+sum(c[0:len(b)])
    a.extend(c[len(b):])
else:
    ans+=sum(c)+sum(b[0:len(c)])
    a.extend(b[len(c):])
a.sort(reverse=True)
ans+=sum(a[0:len(d)])
print(ans)