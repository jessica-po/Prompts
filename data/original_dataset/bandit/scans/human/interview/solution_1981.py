n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = [0] + [set() for i in range(n) ]
k = 0
f = [0] * (n + 1)
f[1] = a[1]
for i in range(n-1):
    x, y = map(int, input().split())
    b[x].add(y)
    b[y].add(x)
    
from collections import deque
d = deque()
d.append(1)
while len(d) > 0:
    t = d.popleft()
    if len(b[t]) == 0:
        if f[t] <= m:
            k += 1
    for i in b[t]:
        b[i].remove(t)
        if a[i] == 0 and f[t] <= m:
            f[i] = 0
        else:    
            f[i] = f[t] + 1
        d.append(i)
print(k)