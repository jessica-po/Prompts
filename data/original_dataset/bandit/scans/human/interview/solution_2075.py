n, m = list(map(int, input().split()))
s = input()
mod = 10 ** 9 + 7
c = b = 0
for x in s:
    c += (x == '(') * 2 - 1
    b = min(c, b)
d = [[1]]
for i in range(n - m):
    nd = d[-1][1:] + [0] * 2
    for j in range(1, i + 2):
        nd[j] = (nd[j] + d[-1][j-1]) % mod
    d.append(nd)
ans = 0
for i in range(n - m + 1):
    l = n - m - i
    for j in range(-b, min(l - c, i) + 1):
        ans = (ans + d[i][j] * d[l][j + c]) % mod
print(ans)