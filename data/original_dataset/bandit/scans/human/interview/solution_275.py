u = v = 0
a, b = input(), input()
n, m = len(a), len(b)
if n > m: b = '0' * (n - m) + b
else: a = '0' * (m - n) + a
for i in range(max(n, m)):
    u, v = v + u, u + int(a[i]) - int(b[i])
    if u > 1:
        print('>')
        return
    elif u < -1:
        print('<')
        return
d = 2 * v + u
if u == v == 0: print('=')
elif u >= 0 and d >= 0: print('>')
elif u <= 0 and d <= 0: print('<')
else: print('>' if (u * u > v * (v + u)) ^ (u < 0) else '<')