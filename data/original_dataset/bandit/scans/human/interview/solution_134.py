n = int(input())
if n % 4 == 0:
    temp = n // 4
    m = temp * 3
    k = temp * 5
elif n % 2 == 0:
    n //=  2
    m = n**2 // 2
    k = m + 1
    m *= 2
    k *= 2
else:
    m = n**2 // 2
    k = m + 1
if 3 > n:
    print("-1")
else:
    print(m,k)