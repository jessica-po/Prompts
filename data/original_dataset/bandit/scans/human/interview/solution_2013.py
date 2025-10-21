n, m, k = map(int, input().split())
s = 'U' * (n - 1)
s += 'L' * (m - 1)
for i in range(n):
    if (i % 2 == 0):
        s += 'R' * (m - 1)
    else:
        s += 'L' * (m - 1)
    if i != n - 1:
        s += 'D'
print(len(s))
print(s)