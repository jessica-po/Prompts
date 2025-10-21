n, m = [int(x) for x in input().split()]

c = 0
for _ in range(n):
    a = [int(x) for x in input().split()]
    for i in range(m):
        if a[i * 2] or a[i * 2 + 1]:
            c += 1

print(c)