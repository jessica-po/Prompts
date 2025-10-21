a, d = list(map(float, input().split()))
n = int(input())

def coordinates(s):
    if s <= a:
        return (s, 0)
    elif s <= 2*a:
        return (a, s-a)
    elif s <= 3*a:
        return (3*a - s, a)
    else:
        return (0, 4*a - s)

for i in range(1, n+1):
    print("%f %f" % coordinates(i*d % (4*a)))