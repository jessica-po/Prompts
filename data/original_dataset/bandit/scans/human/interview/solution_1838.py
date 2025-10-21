n,m,q=list(map(int,input().split()))
a=input().split()
c={x:([x],[]) for x in a}
for i in range(m):
    t,x,y=input().split()
    if t=='2':
        sign=1
    else: sign=0
    if c[x][0] is c[y][1-sign]:
        print("NO")
        continue
    print("YES")
    if c[x][0] is c[y][sign]:
        continue
    c1,c2=c[x],c[y]
    if len(c1[0])+len(c1[1])<len(c2[0])+len(c2[1]):
        c1,c2=c2,c1
    s1,a1=c1
    if sign==0:
        s2,a2=c2
    else:
        a2,s2=c2
    s1+=s2
    a1+=a2
    cs=s1,a1
    for x in s2:
        c[x]=cs
    ca=a1,s1
    for x in a2:
        c[x]=ca
for i in range(q):
    x,y=input().split()
    if c[x][0] is c[y][0]:
        print(1)
    elif c[x][0] is c[y][1]:
        print(2)
    else:
        print(3)