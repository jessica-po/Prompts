import math

n = int(input())
x = [int(k) for k in input().split(" ")]
m = x[0]
chk = [max(0,(x[i]%m)) for i in range(n)]

if sum(chk) > 0:
    print(-1)
else:
    print(2*n-1)
    o = []
    o.append(str(m))
    for i in range(1,n):
        o.append(str(x[i]))
        o.append(str(m))

    print(" ".join(o))