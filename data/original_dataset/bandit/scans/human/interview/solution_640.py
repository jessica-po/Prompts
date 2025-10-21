a, b = list(map(int, input().split()))
res = [0,0,0]
for i in range(1, 7):
    if abs(a - i) < abs(b - i):
        res[0] += 1
    elif abs(a - i) == abs(b - i):
        res[1] += 1
    else:
        res[2] += 1
print(' '.join(map(str, res)))