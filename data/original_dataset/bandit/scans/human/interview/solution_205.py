n, k = map(int, input().split())
a = []
i = 2
while (i * i <= k):
    if (k % i == 0):
        a.append([i, 0])
        while (k % i == 0):
            a[len(a) - 1][1] += 1
            k //= i
    i += 1
if (k > 1):
    a.append([k, 1])
ans = 10 ** 20
for i in a:
    cnt = 0
    x = i[0]
    while (x <= n):
        cnt += n // x;
        x *= i[0]
    ans = min(ans, cnt // i[1])
print(ans)