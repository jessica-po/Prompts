n, k1, k2 = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
r = sorted([abs(a[i] - b[i]) for i in range(n)], reverse=True)
for it in range(k1 + k2):
    if r[0] == 0:
        r[0] = 1
    else:
        r[0] -= 1
        for i in range(n - 1):
            if r[i] < r[i + 1]:
                r[i], r[i + 1] = r[i + 1], r[i]
print(sum(x**2 for x in r))