n = int(input())
a = [-1]*100001
p = 0
for i in range(n):
    x, k = map(int, input().split())
    if a[k] < x-1:
        p = 1
    else:
        a[k] = max(a[k],x)
if p:
    print('NO')
else:
    print('YES')