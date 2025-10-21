x,y,z = list(map(int,input().split()))
a,b,c = list(map(int,input().split()))
if a < x:
    print("NO")
    return
x -= a
y += x
if b < y:
    print("NO")
    return
y -= b
z += y
if c < z:
    print("NO")
    return
print("YES")