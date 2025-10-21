read = lambda: map(int, input().split())
n, k, p = read()
a, b = sorted(read()), sorted(read())
print(min(max(abs(b[i + d] - a[i]) + abs(b[i + d] - p) for i in range(n)) for d in range(k - n + 1)))