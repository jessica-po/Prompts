ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())

from collections import defaultdict as dd

n = ii()
a, b = input().strip(), input().strip()
da, db = dd(list), dd(list)
qa, qb = [], []
for i in range(n):
    if a[i] == '?':
        qa.append(i)
    else:
        da[a[i]].append(i)
    if b[i] == '?':
        qb.append(i)
    else:
        db[b[i]].append(i)

ans = []
for c in 'abcdefghijklmnopqrstuvwxyz':
    u, v = da[c], db[c]
    while u and v:
        ans.append((u.pop(), v.pop()))
    while u and qb:
        ans.append((u.pop(), qb.pop()))
    while v and qa:
        ans.append((qa.pop(), v.pop()))
while qa and qb:
    ans.append((qa.pop(), qb.pop()))

print(len(ans))
print(*('%d %d' % (i + 1, j + 1) for i, j in ans), sep='\n')