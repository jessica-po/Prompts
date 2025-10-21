s = input()
t = input()
a, b = int(s[:2]), int(s[3:])
c, d = int(t[:2]), int(t[3:])
a -= c
b -= d
if b < 0:
    a -= 1
    b = 60 + b
if a < 0:
    a = 24 + a
if a < 10:
    print(0, end = '')
print(a, ':', end = '', sep = '')
if b < 10:
    print(0, end = '')
print(b)