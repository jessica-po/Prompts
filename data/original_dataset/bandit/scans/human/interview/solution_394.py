n = int(input())
a = list(map(int, input().split()))
ans = []

for k in range(1, n + 1):
    x = [0] * k

    x[0] = a[0]
    for i in range(1, k):
        x[i] = a[i] - a[i - 1]

    ok = True
    for i in range(k, n):
        if x[i % k] != a[i] - a[i - 1]:
            ok = False
            break
    if ok:
        ans.append(k)

print(len(ans))
print(*ans)