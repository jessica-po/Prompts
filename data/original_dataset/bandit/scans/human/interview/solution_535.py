def primeFactor(N):
    i = 2
    ret = {}
    n = N
    mrFlg = 0
    if n < 0:
        ret[-1] = 1
        n = -n
    if n == 0:
        ret[0] = 1
    while i**2 <= n:
        k = 0
        while n % i == 0:
            n //= i
            k += 1
            ret[i] = k
        if i == 2:
            i = 3
        else:
            i += 2
        if i == 101 and n >= (2**20):
            def findFactorRho(N):
                # print("FFF", N)
                def gcd(a, b):
                    if b == 0:
                        return a
                    else:
                        return gcd(b, a % b)
                def f(x, c):
                    return ((x ** 2) + c) % N
                semi = [N]
                for c in range(1, 11):
                    x=2
                    y=2
                    d=1
                    while d == 1:
                        x = f(x, c)
                        y = f(f(y, c), c)
                        d = gcd(abs(x-y), N)
                    if d != N:
                        if isPrimeMR(d):
                            return d
                        elif isPrimeMR(N//d):
                            return N//d
                        else:
                            semi.append(d)

                semi = list(set(semi))
                # print (semi)
                s = min(semi)
                for i in [2,3,5,7]:
                    while True:
                        t = int(s**(1/i)+0.5)
                        if t**i == s:
                            s = t
                            if isPrimeMR(s):
                                return s
                        else:
                            break

                i = 3
                while True:
                    if s % i == 0:
                        return i
                    i += 2
                    
            while True:
                if isPrimeMR(n):
                    ret[n] = 1
                    n = 1
                    break
                else:
                    mrFlg = 1
                    j = findFactorRho(n)
                    k = 0
                    while n % j == 0:
                        n //= j
                        k += 1
                        ret[j] = k
                if n == 1:
                    break
        
    if n > 1:
        ret[n] = 1
    if mrFlg > 0:
        def dict_sort(X):
            Y={}
            for x in sorted(X.keys()):
                Y[x] = X[x]
            return Y
        ret = dict_sort(ret)
    return ret

def isPrime(N):
    if N <= 1:
        return False
    return sum(primeFactor(N).values()) == 1

def isPrimeMR(n):
    # print("MR", n)
    if n == 2: return True
    if n == 1 or n & 1 == 0: return False

    d = (n - 1) >> 1
    while d & 1 == 0:
        d >>= 1

    for a in [2, 3, 5, 7, 11, 13, 17, 19]:
        t = d
        y = pow(a, t, n)

        while t != n - 1 and y != 1 and y != n - 1:
            y = (y * y) % n
            t <<= 1

        if y != n - 1 and t & 1 == 0:
            # print("not prime")
            return False
    # print("prime")
    return True        

def findPrime(N):
    if N < 0:
        return -1
    i = N
    while True:
        if isPrime(i):
            return i
        i += 1

def divisors(N):
    pf = primeFactor(N)
    ret = [1]
    for p in pf:
        ret_prev = ret
        ret = []
        for i in range(pf[p]+1):
            for r in ret_prev:
                ret.append(r * (p ** i))
    return sorted(ret)

def mxpow(m, a, e):
    if e == 1:
        return a
    if e % 2 == 0:
        tmp = mxpow(m, a, e//2)
        return mxprod(m, tmp, tmp)
    else:
        tmp = mxpow(m, a, e//2)
        return mxprod(m, mxprod(m, tmp, tmp), a)

def mxprod(m, a, b):
    ret = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            for k in range(m):
                ret[i][j] += a[i][k] * b[k][j]
                ret[i][j] %= P
    return ret

def mxv(m, a, v):
    ret = [0]*m
    for i in range(m):
        for k in range(m):
            ret[i] += a[i][k] * v[k]
            ret[i] %= P
    return ret

def mx(m):
    ret = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(i, m):
            ret[i][j] = inv(j+1)
            
    return ret
    
def vc(m):
    return [0] * (m-1) + [1]


def inv(a):
    return pow(a, P-2, P)


# ----- -----

P = 10**9 + 7

n, k = list(map(int, input().split()))
# n = 6
# k = 2

pf = primeFactor(n)
# print(pf)

ans = 1
for p in pf:
    m = pf[p] + 1
    vvv = mxv(m, mxpow(m, mx(m), k), vc(m))

    t = 0
    for i in range(m):
        t += (vvv[i] * p ** i) % P
        t %= P
        
    ans *= t
    ans %= P
print(ans)