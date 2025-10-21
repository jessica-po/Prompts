def i23(x):
    while x%2==0:
        x//=2
    while x%3==0:
        x//=3
    return x == 1
import fractions
from fractions import gcd
x = int(input())
y = list(map(int, input().split(' ')))

gcdx = y[0]
for i in y:
    gcdx = gcd(i, gcdx)

for i in y:
    if not i23(i/gcdx):
        print("No")
        quit()
print("Yes")