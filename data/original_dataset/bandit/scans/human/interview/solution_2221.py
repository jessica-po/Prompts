x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
n = int(input())
s = input()
psx = [0 for i in range(n)]
psy = [0 for i in range(n)]

if s[0] == 'L':
    psx[0] = -1
elif s[0] == 'R':
    psx[0] = +1

if s[0] == 'D':
    psy[0] = -1
elif s[0] == 'U':
    psy[0] = +1

for i in range(1, n):
    psx[i] = psx[i-1]
    psy[i] = psy[i-1]
    
    if s[i] == 'L':
        psx[i] += -1
    elif s[i] == 'R':
        psx[i] += +1
    
    if s[i] == 'D':
        psy[i] += -1
    elif s[i] == 'U':
        psy[i] += +1

def valid(step):
    cycle = step // n
    rem = step % n
    x = x1
    y = y1
    x += psx[n-1] * cycle
    y += psy[n-1] * cycle
    if rem > 0:
        x += psx[rem-1]
        y += psy[rem-1]
    ManhattanDistance = abs(x - x2) + abs(y - y2)
    return (ManhattanDistance <= step)
    
def binsearch(top, bot):
    res = -1
    while top <= bot:
        mid = (top + bot) // 2
        if valid(mid):
            res = mid
            bot = mid - 1
        else:
            top = mid + 1
    return res
    

print(binsearch(0, 1000000000000000000))