t, s, q = [int(i) for i in input().split()]
a = 1
l = 0
while t > s:
    l += q
    l = min(l, t)
    s += q - 1
    s = min(s, t)
    if l >= s and s != t:
        a += 1
        l = 0
print(a)