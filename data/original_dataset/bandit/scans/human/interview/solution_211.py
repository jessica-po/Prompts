MOD = 1000000009

n,m,k = [int(x) for x in input().split()]

num0 = n-m
num1fin = num0*(k-1)
if num1fin >= m:
    print(m)
else:
    num1open = m-num1fin
    sets = num1open//k
    rem = num1open%k
    print(((pow(2,sets,MOD)-1)*2*k+rem+num1fin)%MOD)