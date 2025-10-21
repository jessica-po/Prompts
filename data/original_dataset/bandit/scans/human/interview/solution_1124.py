import math


def LI():
    return list(map(int, input().split()))


N = int(input())
A = LI()
Amin = min(A)
ans = Amin
for i in A:
    if Amin == i:
        continue
    Amin = min(Amin, math.gcd(Amin, i))
ans = min(ans, math.gcd(Amin, ans))

print(ans)