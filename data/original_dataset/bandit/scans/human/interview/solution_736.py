# 272 D2 A

def func(p,m,n):
    w = p
    while w % m != 0 and w<=n:
        w += 1
    if w<= n:
        return w
    else:
        return -1


    
l = input().split()
n = int(l[0])
m = int(l[1])

if n % 2 == 0:
    p = int(n/2)
else:
    p = int(n/2)+1

print(func(p,m,n))