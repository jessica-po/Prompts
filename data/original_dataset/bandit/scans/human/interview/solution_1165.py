import collections
import math

n ,m = map(int, input().split())
A = list(map(int, input().split()))
ans, f = [], [0] * n
f[0] = -1
for i in range(1, n):
    if A[i] != A[i - 1]:
        f[i] = i - 1
    else:
        f[i] = f[i - 1]
for i in range(m):
    l, r, x = map(int, input().split())
    #q.append([l - 1, r - 1, x])
    #for i in range(m):
    if A[r - 1] != x:
        ans.append(r)
    elif f[r - 1] >= l - 1:
        ans.append(f[r - 1] + 1)
    else:
        ans.append(-1)
print('\n'.join(str(x) for x in ans))