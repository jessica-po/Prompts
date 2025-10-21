L = lambda: list(map(int, input().split()))
I = lambda: int(input())

n, t = I(), [L() for i in range(4)]
p = [min(i[0], i[1]) + min(i[2], i[3]) for i in t]
x = min(p)
if x > n: print(-1)
else:
    k = p.index(x)
    p = min(t[k][0], t[k][1])
    print(k + 1, p, n - p)