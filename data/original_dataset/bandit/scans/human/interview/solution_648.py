read = lambda: map(int, input().split())
m, b = read()
ans = -1
def f(x, y):
    return (x * (x + 1) * (y + 1) + y * (y + 1) * (x + 1)) // 2
for k in range(b + 3):
    x = k * m
    y = b - k
    ans = max(ans, f(x, y))
print(ans)