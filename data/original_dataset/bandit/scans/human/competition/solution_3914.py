read = lambda: list(map(int, input().split()))
n, d, b = read()
d += 1
t, a = 0, [0] * (n + 1)
for i, x in enumerate(read()):
    t += x
    a[i + 1] = t
print(max(i - min(a[min(n, i * d)], (a[n] - a[max(0, n - i * d)])) // b for i in range(n + 3 >> 1)))