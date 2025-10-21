n, m = map(int, input().split())
t = input()
a, b = t.count('1'), t.count('-')
t = ['0'] * m
c = 2 * min(a - b, b)
for i in range(m):
    l, r = map(int, input().split())
    r -= l
    if r & 1 and r < c: t[i] = '1'
print('\n'.join(t))