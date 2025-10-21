a, b, c, d = list(map(int, input().split()))
print((a * 1.0) / (b * (1 - ((d - c) * (b - a) * 1.0) / (d * b))))