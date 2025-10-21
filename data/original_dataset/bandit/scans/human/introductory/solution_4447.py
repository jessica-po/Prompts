import bisect

n, m = map(int, input().split())
ls = list(map(int, input().split()))

mls = []
for i in range(0, n):
    mls.append((ls[i] % m, i))

mls.sort()
# print(mls)

bk1 = set()
bk2 = set()

aim = n // m
cnt = 0

mis = []
for i in range(m):
    for j in range(aim):
        mis.append(i)

p1 = 0
p2 = 0

while p2 < n:
    if mls[p1][0] > mis[p2]:
        p2 += 1
    else:
        a = mis[p2] - mls[p1][0]
        ls[mls[p1][1]] += a
        cnt += a
        bk2.add(p2)
        p1 += 1
        p2 += 1

if p1 < n and p2 == n:
    p1 = n
    for i in range(p2):
        if i not in bk2:
            p1 -= 1
            a = m - mls[p1][0] + mis[i]
            ls[mls[p1][1]] += a
            cnt += a

print(cnt)
for i in ls:
    print(i, end=' ')