ii = lambda: int(input())
mi = lambda: list(map(int, input().split()))
li = lambda: list(mi())

a, b, c, d = mi()
a, b, c = sorted([a, b, c])
ans = max(0, d - (b - a)) + max(0, d - (c - b))
print(ans)