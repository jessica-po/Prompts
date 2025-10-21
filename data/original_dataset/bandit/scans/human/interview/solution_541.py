n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

ab = sorted(ab, key=lambda x: x[1])
s = ab[0][1]
ans = 1
for i in ab:
    if s <= i[0]:
        ans += 1
        s = i[1]
print(ans)