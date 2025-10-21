n = int(input())
a = [int(i) for i in input().split()]
a.sort()
b = []
for i in range(n - 1, (n + 1) // 2 - 1, -1):
    b.append(a[i])
a = a[:(n + 1) // 2]
c = []
for i in range(len(b)):
    c.append(a[i])
    c.append(b[i])
if len(a) > len(b):
    c.append(a[-1])
print(*c)