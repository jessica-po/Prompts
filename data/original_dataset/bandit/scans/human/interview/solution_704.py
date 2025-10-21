import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

n = int(input())
a = list(map(int, input().split()))

r1, c1, r2, c2 = (i - 1 for i in map(int, input().split()))
x, y = (r1, r2) if r1 < r2 else (r2, r1)

if r1 < r2: c1 = min(c1, min(a[i] for i in range(r1 + 1, r2 + 1)))
elif r2 < r1: c1 = min(c1, min(a[i] for i in range(r2, r1)))

d = abs(c1 - c2)
c = c1
for i in range(x - 1, -1, -1):
    if c > a[i]:
        c = a[i]
        q = abs(c2 - c) + 2 * abs(x - i)
        if q < d: d = q
c = c1
for i in range(y + 1, n):
    if c > a[i]:
        c = a[i]
        q = abs(c2 - c) + 2 * abs(i - y)
        if q < d: d = q
print(d + abs(r2 - r1))