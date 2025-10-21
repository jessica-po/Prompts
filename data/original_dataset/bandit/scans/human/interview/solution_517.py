import string

i = input()
i = i.split(' ')
n, d, h = list([int(x) for x in i])

def check(n, d, h):
    if d > 2 * h:
        print(-1)
        return

    if d < h:
        print(-1)
        return
    if n < d + 1 or n < h + 1:
        print(-1)
        return
    if d == 1 and n > 2:
        print(-1)
        return

out = []
#h
check(n, d, h)
c = 0
# print('h')
for i in range(h):
    out.append(str(c + 1) + ' ' + str(c + 2))
    # print(out[-1])
    c += 1
c += 1
c1 = 0
# print('d')
for i in range(d - h):
    out.append(str(c1 + 1) + ' ' + str(c + 1))
    # print(out[-1])
    c1 = c
    c += 1

c += 1
# print('n')
if d == h:
    s = 2
else:
    s = 1
    
for i in range(n - c + 1):
    out.append(str(s) + ' ' + str(c))
    # print(out[-1])

    c += 1

for el in out:
    print(el)