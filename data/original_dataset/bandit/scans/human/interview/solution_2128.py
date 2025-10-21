#q = int(input())
#x, y = map(int,input().split(' '))
#print (' '.join(list(map(str, s))))

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
 
def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m

m = 998244353
n = int(input())
p = list(map(int,input().split(' ')))

up = 0
low = 1
for i in range(n):
    up = up + low
    up = up * 100 % m
    low = low * p[i] % m
    
print (up*modinv(low,m)%m)