n = int(input())
m = (n + 2) // 2
d = [0, 1]
print(m)
for i in range(1, n + 1):
    if d[0] < m:
        d[0] += 1
        print(*d)
    else:
        d[1] += 1
        print(*d)