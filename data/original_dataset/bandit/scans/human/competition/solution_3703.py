from math import sqrt, ceil

MAX_N = 10 ** 6 * 2 


prime = []
isPrime = [True for i in range(MAX_N)]

for i in range(2, MAX_N):
    if isPrime[i]:
        prime.append(i)
        for j in range(i * i, MAX_N, i):
            isPrime[j] = False


def factor(a):
    divs = []
    for i in prime:
        cnt = 0
        while a % i == 0:
            a //= i
            cnt += 1

        if cnt:
            divs.append((i, cnt,))

    if a > 1:
        divs.append((a, 1,))

    return divs


def f(n):
    ans = 1
    for div in factor(n):
        ans *= div[0] ** (div[1] - 1) * (div[0] - 1)

    return ans

def g(n):
    return n

def F(n, k):
    cur = n
    for i in range(1, k + 1):
        #print(i)
        #print(factor(cur))
        if i == 1:
            cur = f(g(cur))
        elif i % 2 == 0:
            cur = g(cur)
        else:
            cur = f(cur)

        #print(i, cur)

        if cur == 1:
            break

    return cur % (10 ** 9 + 7)

n, k = [int(i) for i in input().split(' ')]
#print(factor(n - 1))
print(F(n, k))