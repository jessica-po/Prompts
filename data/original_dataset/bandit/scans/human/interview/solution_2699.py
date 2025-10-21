# cook your dish here
a=int(input())
p=list(map(int,input().split()))
for n in p:
    # n=int(input())
    a=[1]
    b=[2]
    c=[4]
    d=[3]
    j=1
    k=1
    for i in range(n-1):
        a.append(a[i]+3*(j))
        b.append(b[i]+3*(j))
        c.append(c[i]+6*(j))
        d.append(d[i]+3*(j))
        j*=2
        # k+
    print(*a)
    print(*b)
    print(*c)
    print(*d)