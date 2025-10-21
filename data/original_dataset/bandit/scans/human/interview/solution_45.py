n, k = map(int, input().split())
div = []
i = 1
n1 = n
while i * i <= n:
    if n % i == 0:
        div.append(i)
        div.append(n // i)
    i += 1
div.sort()
mx = -1
for i in range(len(div)):
    a = div[i] * k * (k + 1) // 2
    if a <= n:
        mx = div[i]
if mx == -1:
    print(-1)
else:
    for i in range(k - 1):
        print(mx * (i + 1), end= " ")
    print(n - mx * k * (k - 1) // 2)