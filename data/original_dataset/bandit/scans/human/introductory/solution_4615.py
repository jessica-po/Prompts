a, b, c, d, e, f = map(int, input().split())
s = set()
for i in range(30 // a + 1):
    for j in range(30 // b + 1):
        if 0 < (a * i + b * j) * 100 <= f:
            s = s | {a * i + b * j}
s2 = set()
for i in range(3000 // c + 1):
    for j in range(3000 // d + 1):
        if c * i + d * j <= f:
            s2 = s2 | {c * i + d * j}
ans = []
for i in s:
    for j in s2:
        if i * 100 + j <= f and j <= i * e:
            ans.append([j / i * -1, i * 100 + j, j])
ans.sort()
print(ans[0][1], ans[0][2])