x,y = [int(x) for x in input().split()]
if x*y > 0:
    if x < 0:
        print(x+y,0,0,x+y)
    else:
        print(0,x+y,x+y,0)
else:
    if x < 0:
        print(x-y,0,0,y-x)
    else:
        print(0,y-x,x-y,0)