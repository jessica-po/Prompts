n, p = int(input()), list(map(int, input().split()))
a, c, v = [0] * n, 1, 1
for i, pi in enumerate(p):
    a[pi - 1] = i
for i in range(n - 1):
    if a[i] < a[i + 1]:
        c += 1
        if c > v:
            v = c
    else:
        c = 1
print(n - v)