for i in range(int(input())):
    t = input().split(':')
    if t[-1] == '': t.pop()
    elif t[0] == '': t.pop(0)
    if '' in t: t[t.index('')] = ('0000:' * (9 - len(t)))[: -1]
    print(':'.join('0' * (4 - len(i)) + i for i in t))