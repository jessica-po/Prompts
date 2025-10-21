ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())

n = ii()
a = [li() for _ in range(n)]
k = ii()
ans = 0
for l, r in a:
    ans += k <= r
print(ans)