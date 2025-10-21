n, l, r = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
d = []

isOk = 0

for i in range(0, l - 1):
    if a[i] != b[i]:
        isOk = 1

for i in range(r, n):
    if a[i] != b[i]:
        isOk = 1

for i in range(l - 1, r):
    c.append(a[i])
    d.append(b[i])

c.sort()
d.sort()

if c != d:
    isOk = 1

if isOk == 1:
    print("LIE")
else:
    print("TRUTH")