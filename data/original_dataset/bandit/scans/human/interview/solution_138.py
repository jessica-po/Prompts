n, a, b, c = map(int, input().split())
res = 10 ** 100
for i in range(50):
    for j in range(50):
        for k in range(50):
            if (n + i + 2 * j + 3 * k) % 4 == 0:
                res = min(res, a * i + b * j + c * k)
print(res)