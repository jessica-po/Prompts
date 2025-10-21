# 素因数分解
def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
# かけらを移動させて共通因数を持つようにする
su = sum(A)
if su == 1:
    print(-1)
    return
primes = sorted(set(prime_decomposition(su)))
ans = 10**18

for p in primes:
    an = 0
    half = p >> 1
    cnt = 0
    for a in A:
        a %= p
        cnt += a
        if cnt <= half:
            an += cnt
        else:
            if cnt < p:
                an += p - cnt
            else:
                cnt -= p
                if cnt <= half:
                    an += cnt
                else:
                    an += p - cnt
        if ans <= an:
            break
    else:
        ans = min(ans, an)
print(ans)