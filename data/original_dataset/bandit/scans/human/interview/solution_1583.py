import math
a, b, x = map(int,input().split())
s = a
t = 2*(b-x/(a*a))
u = x*2/(b*a)
if t<=b:
    print(math.degrees(math.atan(t/s)))
else:
    print(math.degrees(math.atan(b/u)))