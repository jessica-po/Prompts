a, b = map(int, input().split())
d, c = map(int, input().split())
print(max(abs(a - d), abs(b - c)))