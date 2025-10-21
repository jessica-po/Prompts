from math import ceil

p,x,y = map(int, input().split())
h = x
while h >=y:
    h-=50
h+=50
for i in range(h, 10000000000, 50):
    u = (i//50)%475
    d = []
    for j in range(25):
        u = (u * 96 + 42)%475
        d.append(26 + u)
    if p in d:
        k = i
        break
if k-x>0:
    print(ceil((k-x)/100))
else:
    print(0)