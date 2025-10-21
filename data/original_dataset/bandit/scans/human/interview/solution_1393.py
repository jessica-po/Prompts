def upc(c):
    if c >= 'a' and c <= 'z':
        c = chr(ord(c) - ord('a') + ord('A'))
    return c
a1, a2 = {}, {}
for i in input():
    if i in a1:
        a1[i] += 1
    else:
        a1[i] = 1
for i in input():
    if i in a2:
        a2[i] += 1
    else:
        a2[i] = 1
r1, r2 = 0, 0
a3, a4 = {}, {}
for k in a1:
    v = a1[k]
    if not k in a2:
        continue
    c = min(v, a2[k])
    a2[k] -= c
    a1[k] -= c
    r1 += c
for k in a1:
    v = a1[k]
    c = upc(k)
    if c in a3:
        a3[c] += v
    else:
        a3[c] = v
for k in a2:
    v = a2[k]
    c = upc(k)
    if c in a4:
        a4[c] += v
    else:
        a4[c] = v
for k in a3:
    if not k in a4:
        continue
    v = a3[k]
    c = min(v, a4[k])
    a3[k] -= c
    a4[k] -= c
    r2 += c
print(r1, r2)