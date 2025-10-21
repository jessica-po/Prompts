N = int(input())
mod = 1000000007
from collections import Counter
Y = Counter()
for i in range(2, N+1):
    M = i
    for j in range(2,i+1):
        while M % j == 0:
            Y[j] += 1
            M //= j

def product(X):
    res = 1
    for x in X:
        res *= x + 1
        res %= mod
    return res    

ans = product(Y.values())
print(ans)