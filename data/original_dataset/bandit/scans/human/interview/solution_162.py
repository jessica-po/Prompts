n, k = map(int, input().split())
a = list(map(int, input().split()))

maxd = -1
for x in a:
    if k % x == 0:
        maxd = max(maxd, x)
print(k // maxd)