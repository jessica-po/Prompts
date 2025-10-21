a = list(map(int, input().split()))
s = sum(a)
for i in range(6):
    for j in range(i):
        for k in range(j):
            ss = a[i] + a[j] + a[k]
            if ss == s - ss:
                print('YES')
                return
print('NO')