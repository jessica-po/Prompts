n = int(input())
a = []
for i in range(1, n + 1):
    l, r = list(map(int, input().split()))
    a.append([l, -r, i])
a.sort()
hh = a[0][1]
wahh = max(-1, a[0][2])
for i in range(1, n):
    if a[i][1] >= hh:
        print(a[i][2], wahh)
        return
    else:
        hh = a[i][1]
        wahh = a[i][2]
print(-1, -1)