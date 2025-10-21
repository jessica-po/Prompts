from math import ceil

hh, mm = [int(x) for x in input().split()]

h, d, c, n = [int(x) for x in input().split()]

cost = 0.8 * c if hh >= 20 else c

res = int(ceil(h / n)) * cost

if hh < 20:
    diff = (20 - hh) * 60 - mm
    diff *= d
    h += diff
    res = min(res, int(ceil(h / n)) * 0.8 * c)
    
print(res)