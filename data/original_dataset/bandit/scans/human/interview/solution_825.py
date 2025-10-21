def division(n):
    if n < 2:
        return []
    prime_fac = []
    for i in range(2,int(n**0.5)+1):
        cnt = 0
        while n % i == 0:
            n //= i
            cnt += 1
        if cnt!=0:prime_fac.append((i,cnt))
    if n > 1:
        prime_fac.append((n,1))
    return prime_fac

n = int(input())
div = division(n)
ans = 0
for i,e in div:
    b = 1
    while b <= e:
        e -= b
        b += 1
        ans += 1
print(ans)