r = open('input.txt')
w = open('output.txt', mode='w')

f = lambda: map(int, r.readline().split())

f()
a, b = f()
if a > b: a, b = b, a
n = 40001
u, v = [n] * n, [n] * n
x = s = 0
u[0] = v[0] = 0

for y in f():
    s += y
    p = []
    h = min(x, y)
    for d in range(min(s, a), max(0, s - b - y) - 1, -1):
        t = v[d]

        if u[d] != n:
            u[d + y] = min(u[d], u[d + y])
            v[d] = min(t, u[d] + h)
            u[d] = n

        if t != n:
            u[d + y] = min(u[d + y], t + h)
    x = y

i = max(s - b, 0)
j = min(s, a) + 1

d = min(u[i:j] + v[i:j]) if i < j else n
w.write(str(d if d < n else -1))

w.close()
r.close()