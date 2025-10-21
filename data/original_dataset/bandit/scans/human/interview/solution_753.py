from fractions import Fraction,gcd

a,b,c,d = [int(x) for x in input().split()]

if a*d > b*c:
    num = a*d-b*c
    denom = a*d
else:
    num = b*c-a*d
    denom = b*c
div = gcd(num,denom)
print('%d/%d'%(num//div,denom//div))