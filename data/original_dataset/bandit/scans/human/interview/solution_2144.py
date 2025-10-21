from math import gcd

def Fenjie(n):
    k = {}
    if (n == 1):
        return {}
    a = 2
    while (n >= 2):
        if (a*a > n):
            if (n in k):
                k[n] += 1
            else:
                k[n] = 1
            break
        b = n%a
        if (b == 0):
            if (a in k):
                k[a] += 1
            else:
                k[a] = 1
            n = n//a
        else:
            a += 1
    return k

def Euler(n):
    if (n == 1):
        return 1
    k = Fenjie(n)
    m = n
    for i in k:
        m = m // i * (i-1)
    return m

t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))
    b = b//gcd(a,b)
    print(Euler(b))