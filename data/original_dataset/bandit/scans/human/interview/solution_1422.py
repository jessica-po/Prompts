p, m = [i for i, x in enumerate(input(), 1) if x == '1'], int(input())
r, q = [(-1, 0, 0, [])], 'NO'
while r:
    x, d, s, t = r.pop()
    if s == m: 
        q = 'YES\n' + ' '.join(map(str, t))
        break
    for y in p:
        if y != x and y > d: r.append((y, y - d, s + 1, t + [y]))
print(q)