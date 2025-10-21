n, m = map(int, input().split())
x = list(map(int, input().split()))

foo = [0 for _ in range(2+n)]

for i in range(1, m) :
    p, q = x[i-1], x[i]

    if p == q : continue

    r = min(p, q)

    s = max(p, q)

    foo[0] += abs(p-q)
    foo[r] -= abs(p-q)
    foo[r] += max(p, q) - 1
    foo[r+1] -= max(p, q) - 1

    foo[r+1] += abs(p-q)-1
    foo[s] -= abs(p-q)-1

    foo[s] += min(p, q)
    foo[s+1] -= min(p, q)

    foo[s+1] += abs(p-q)
    foo[n+1] -= abs(p-q)

    # print(p, q, foo)

for i in range(1,n+1) :
    foo[i] += foo[i-1]
    print(foo[i], end=' ')
print()