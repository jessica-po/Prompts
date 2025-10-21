import sys
f = sys.stdin
# f = open("input.txt", "r")
y, k, n = map(int, f.readline().strip().split())

if y >= n:
    first = -1
else:
    t = k
    while t <= y:
        t += k
    first = t-y
if first == -1:
    print(-1)
else:
    if first+y > n:
        print(-1)
    else:
        res = []
        for i in range(first, n+1-y, k):
            res.append(i)
        print(*res)