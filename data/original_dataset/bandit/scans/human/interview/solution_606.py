import sys

R,x,y,s,t = list(map(int,input().split()))

if (s-x)**2 + (t-y)**2 > R*R:
    print(x,y,R)
    return

dx = x - s
dy = y - t
r = (dx**2 + dy**2)**.5

if abs(r)<1e-9:
    dx = 1
    dy = 0
else:
    dx /= r
    dy /= r

a = s + dx*(R + r)/2
b = t + dy*(R + r)/2

print(a,b,(R+r)/2)