n, k = map(int, input().split())
m = 2 * (n - 1) - k * (k - 1)
if m > 0: print(-1)
else:
    x = int((1 + (1 - 4 * m) ** 0.5) / 2)
    while x * x - x + m > 0: x -= 1
    print(k - x)