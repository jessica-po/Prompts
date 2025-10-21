a, b, c, d = list(map(int, input().split()))
s = max(a, c)
e = min(b, d)
print((e - s if e-s > 0 else 0))