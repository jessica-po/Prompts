(a, b), x, y = list(map(int, input().split())), [], 0

def bin(s):
    return str(s) if s <= 1 else bin(s >> 1) + str(s & 1)

def lowbit(s):
    return int('1' + bin(s).split('1')[-1], 2)

for i in reversed(range(b + 1)):
    if y == a:
        break
    if a >= y + lowbit(i):
        x.append(i) 
        y += lowbit(i)

if y == a:
    print( len(x) )
    print( ' '.join(str(i) for i in x) )
else:
    print( -1 )