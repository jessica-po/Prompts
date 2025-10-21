a, b = [0] * 101, [0] * 101
for i in range(int(input())):
    x, y = map(int, input().split())
    a[x] = b[y] = 1
print(min(sum(a), sum(b)))