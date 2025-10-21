import sys

n, m = list(map(int,input().split()))
g = [list(map(int,input().split())) for _ in range(n)]
for c1 in range(m):
    for c2 in range(c1, m):
        ok = True
        for row in g:
            row[c1], row[c2] = row[c2], row[c1]
            cnt = 0
            for i in range(m):
                if row[i] != i + 1:
                    cnt += 1
                if cnt > 2:
                    break
            row[c1], row[c2] = row[c2], row[c1]
            if cnt > 2:
                ok = False
                break
        if ok:
            print('YES')
            return
print('NO')