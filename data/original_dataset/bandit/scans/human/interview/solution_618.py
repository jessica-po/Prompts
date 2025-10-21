x = input()
z = input()
a, b = -1, -1
p, q ='', ''
p = x[:x.find('|')]
q = x[x.find('|') + 1:]
n = 0
while n < len(z):
    if len(p) < len(q):
        p += z[n]
    else:
        q += z[n]
    n += 1
if len(p) == len(q):
    print(p, '|', q, sep = '')
else:
    print('Impossible')