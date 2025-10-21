n = int(input())


def test(a, s):
    k = [''] * len(a)
    d = {}
    for i in range(len(a)):
        tof = True
        if a[i] == s[:len(a[i])]:
            if a[i] not in d:
                d[a[i]] = 'P'
                tof = False
                k[i] = 'P'
        if not tof:
            continue
        if a[i] == s[len(s) - len(a[i]):]:
            if a[i] not in d or d[a[i]] == 'P':
                d[a[i]] = 'S'
                tof = False
                k[i] = 'S'
        if tof:
            return [-1]
    return k
        


k = ['', '', '', '']
a = []
for i in range(2 * n - 2):
    s = input()
    a.append(s)
    if len(s) == 1:
        if k[0] == '':
            k[0] = s
        else:
            k[1] = s
    if len(s) == n - 1:
        if k[2] == '':
            k[2] = s
        else:
            k[3] = s
m = k[2] + k[0]
r = test(a, m)
if r != [-1]:
    for i in r:
        print(i, end='')
    return
m = k[2] + k[1]
r = test(a, m)
if r != [-1]:
    for i in r:
        print(i, end='')
    return
m = k[3] + k[0]
r = test(a, m)
if r != [-1]:
    for i in r:
        print(i, end='')
    return
m = k[3] + k[1]
r = test(a, m)
if r != [-1]:
    for i in r:
        print(i, end='')