n = int(input())
ans = 1
i = 2
while i * i <= n:
    if n % i == 0:
        ans *= i
    while n % i == 0:
        n //= i
    i += 1
ans *= n
print(ans)