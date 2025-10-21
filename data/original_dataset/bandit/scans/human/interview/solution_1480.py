n, k = map(int, input().split())
aa = [int(x) for x in input().split()]

nxt = [(i + 1) % n for i in range(n)]
prv = [(i - 1 + n) % n for i in range(n)]

cur = 0
for z in range(k):
    a = aa[z]
    a %= n
    for i in range(a):
        cur = nxt[cur]
    nxt[prv[cur]] = nxt[cur]
    prv[nxt[cur]] = prv[cur]
    print(cur + 1, end=' ')
    cur = nxt[cur]
    n -= 1