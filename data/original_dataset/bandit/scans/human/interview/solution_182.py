a, b, c = list(map(int, input().split()))
x, y, z = list(map(int, input().split()))
col = max(0, x - a) + max(0, y - b) + max(0, z - c)
sum = max(0, (a - x) // 2) + max(0, (b - y) // 2) + max(0, (c - z) // 2)
if sum >= col:
    print('Yes')
else:
    print('No')