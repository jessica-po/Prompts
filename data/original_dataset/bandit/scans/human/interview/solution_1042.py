import sys

x,y = list(map(int, input().strip().split()))

if y % x != 0:
    print(0)
    return

MOD = 10**9 + 7

K = y//x

def multiply(A,b, MOD):
    n, m = len(A), len(b[0])
    matrika = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            vsota = 0
            for k in range(len(A[0])):
                vsota += A[i][k]*b[k][j]
            matrika[i][j] = vsota % MOD
    return matrika

def copy(mat):
    return [e[:] for e in mat]

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    matrika = [[1,1],[1,0]]

    pripravi = dict()
    pripravi[1] = copy(matrika)
    s = 1

    pot = [1]

    working = copy(matrika)
    
    while s <= n:
        working = multiply(working,working,MOD)
        s*= 2
        pripravi[s] = copy(working)
        pot.append(s)

    manjka = n-2
    pointer = len(pot) - 1
    while manjka > 0:
        if pot[pointer] > manjka:
            pointer -= 1
        else:
            matrika = multiply(matrika, pripravi[pot[pointer]], MOD)
            manjka -= pot[pointer]

    v = [[1],[0]]

    return multiply(matrika, v, MOD)[0][0]

memo2 = dict()
def find(y):
    if y in memo2:
        return memo2[y]
    ALL = (pow(2, y - 1, MOD)) % MOD

    k = 2
    while k*k <= y:
        if y % k == 0:
            if k*k != y:
                ALL -= find(y//k)
                ALL -= find(k)
            else:
                ALL -= find(k)
        k += 1
        #print(k, ALL)

    if y != 1:
        ALL -= 1

    memo2[y] = ALL % MOD
    return ALL % MOD

print(find(K) % MOD)


def gcd(x,y):
    if x == 0:
        return y
    if y > x:
        return gcd(y,x)
    if x % y == 0:
        return y
    return gcd(y, x % y)


memo = dict()
def brute(k, gc):
    if (k,gc) in memo:
        return memo[k,gc]
    if k == 0:
        if gc:
            return 1
        else:
            return 0
    ALL = 0
    for i in range(1, k + 1):
        ALL += brute(k-i,gcd(gc,i))
    memo[k, gc] = ALL
    return ALL

#print(brute(K,0) % MOD)