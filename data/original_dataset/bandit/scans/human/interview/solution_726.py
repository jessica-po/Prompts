read = lambda: map(int, input().split())
n, d = read()
x = sorted(read())
ans = 2
for i in range(1, n):
    dx = x[i] - x[i - 1]
    if dx == 2 * d:
        ans += 1
    elif dx > 2 * d:
        ans += 2
print(ans)