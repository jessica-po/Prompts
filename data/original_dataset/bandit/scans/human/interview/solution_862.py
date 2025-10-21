n = int(input())
a = list(map(int, input().split()))
mn = 10000000000
ans = -1
from math import ceil
for i in range(n):
    b = a[i] - i
    c = int(ceil(b / n))
    cc = n*c
    if n*c < mn:
        mn = n*c
        ans = i+1
print(ans)