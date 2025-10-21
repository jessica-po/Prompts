import math

n, k = map(int, input().split())
a = list(map(int, input().split()))
now = [-1] * k
t = [0] * k
nxt = 0
m = 0
intr = [False for i in range(n)]
while m < n:
    for i in range(k):
        if now[i] != 1005 and (now[i] == -1 or t[i] == a[now[i]]):
            if now[i] != -1:
                m += 1
            if nxt == n:
                now[i] == 1005
                t[i] = 1000
            else:
                now[i] = nxt
                nxt += 1
                t[i] = 0
        t[i] += 1
    d = (200 * m + n) // (2 * n)
    for i in range(k):
        if d == t[i]:
            intr[now[i]] = True
print(sum(intr))