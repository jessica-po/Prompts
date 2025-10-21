n, k = list(map(int, input().split()))
result = 10 ** 26
for i in range(1, k):
    if n % i == 0:
        t = n // i
        result = min(result, t * k + i)
print(result)