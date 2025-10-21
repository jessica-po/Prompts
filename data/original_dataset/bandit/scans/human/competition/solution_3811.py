from math import sqrt
def primset(n):
    a = set()
    
    while n % 2 == 0:
        a.add(2)
        n = n//2
         
    for i in range(3,int(sqrt(n))+1,2):
        while n % i== 0:
            a.add(i)
            n = n//i
            
    if n > 2:
        a.add(n)
    return a

n = int(input())
a, b = map(int, input().split())

primes = primset(a)
primes.update(primset(b))

for i in range(1, n):
    a, b = map(int, input().split())
    r = set()
    for p in primes:
        if a%p != 0 and b%p != 0:
            r.add(p)
    for rem in r:
        primes.remove(rem)
    if len(primes) < 1:
        print(-1)
        return
print(primes.pop())