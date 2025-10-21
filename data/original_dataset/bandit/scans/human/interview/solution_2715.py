k = int(input())
n = 50
if k <= n-1:
    aas = [0] * n
    aas[0] += n * k
else:
    t = k // n
    k %= n
    aas = [n-k+t-1] * n
    i = 0
    cnt = 0
    while cnt < k:
        aas[i] += 1 + k
        i += 1
        cnt += 1
print(n)
print(*aas)