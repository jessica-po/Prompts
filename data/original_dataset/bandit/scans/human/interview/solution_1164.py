3

s = input()
alph = ''.join([chr(ord('a') + x) for x in range(26)])
l = [[]]
for x in s:
    if x not in alph:
        l[-1].append(x)
    else:
        if len(l[-1]):
            l.append([])
l = list([''.join(x) for x in l])
ansa = 0
ansb = 0
for t in l:
    if len(t) > 2 and t[-3] == '.':
        ansb += int(t[-2:])
        t = t[:-3]
    ansa += int(''.join(t.split('.')))
ansa += ansb // 100
ansb %= 100
ansa = str(ansa)
ans = []
last = len(ansa)
for x in range(len(ansa) - 3, -1, -3):
    ans.append(ansa[x:last])
    last = x
if last != 0:
    ans.append(ansa[:last])
ans.reverse()
if ansb != 0:
    ans.append("%02d" % ansb)
print(".".join(ans))