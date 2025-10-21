import math

l = int(input()) - 1
n = int(math.log2(l + 1) + 1)
res = []
for i in range(n - 1):
    res.append([i + 1, i + 2, 0])
    res.append([i + 1, i + 2, 2 ** i])
i = n - 2
while l > 2 ** (n - 1) - 1:
    t = l - 2 ** i + 1
    if t > 2 ** (n - 1) - 1:
        res.append([i + 1, n, t])
        l = t - 1
    i -= 1
print((n, len(res)))
for i in range(len(res)):
    print((res[i][0],res[i][1],res[i][2]))