n = int(input())
a = list(map(int, input().split()))
o = [a[i] for i in range(0,n,2)]
e = [a[h] for h in range(1,n,2)]
if n%2 == 0:
    e.reverse()
    l = e + o
    print(*l)
else:
    o.reverse()
    l = o + e
    print(*l)