x, y, z = map(int, input().split())
if z == 0:
    if x == y:
        print('0')
    elif x > y:
        print('+')
    else:
        print('-')
else:
    if x > y + z:
        print('+') 
    elif x + z < y:
        print('-')
    else:
        print('?')