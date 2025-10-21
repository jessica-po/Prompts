n, m = [int(x) for x in input().strip().split()]
c = [int(x) for x in input().strip().split()]
a = [int(x) for x in input().strip().split()]

ans = 0
ai = 0
for ci in c:
    if ai < len(a) and a[ai] >= ci:
        ai += 1
        ans += 1
print(ans)