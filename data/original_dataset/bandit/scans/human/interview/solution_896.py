n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
t1, t2 = 0, 0
for i in a:
    t1 ^= i
for i in b:
    t2 ^= i
if t1 != t2:
    print('NO')
else:
    print('YES')
    for i in range(n-1):
        for j in range(m-1):
            print(0, end=' ')
        print(a[i])
    tmp = 0
    for j in range(m-1):
        print(b[j], end=' ')
        tmp ^= b[j]
    print(a[n-1]^tmp)