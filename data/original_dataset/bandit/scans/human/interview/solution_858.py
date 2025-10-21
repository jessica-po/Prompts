import math 
a = int(input())
if a%2==1:
    print(math.ceil((a-1)/2))
else:
    z = 1
    while z*2<=a:
        z*=2
    print((a-z)//2)