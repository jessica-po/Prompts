s = input()
a = str()
b = str()
f = False
for i in range(len(s)):
    if s[i] == 'e':
        f = True
    elif f:
        b = b + s[i]
    else:
        a = a + s[i]
pos = a.index('.')
n = int(b)
a = list(a)
for i in range(n):
    if pos == len(a) - 1:
        a.append('0')
    a[pos], a[pos + 1] = a[pos + 1], a[pos]
    pos += 1
if a[-1] == '.':
    a.pop()
if '.' in a:
    while a[-1] == '0':
        a.pop()
if a[-1] == '.':
    a.pop()
if '.' not in a:
    while len(a) > 1 and a[0] == '0':
        a.pop(0)
for i in range(len(a)):
    print(a[i], end = '')