def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


n = int(input())
ans = len(make_divisors(n - 1))
divisors = []
for i in make_divisors(n):
    j = n
    if i != 1:
        while j % i == 0:
            j //= i
        if (j - 1) % i == 0:
            divisors.append(i)
print((ans + len(divisors) - 1))