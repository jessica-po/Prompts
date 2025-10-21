import sys

s = input()
qc = s.count('Q')
qs = int(qc ** 0.5)
hc = s.count('H')
if qs == 0:
    print('Yes')
    return
if not qc == qs ** 2:
    print('No')
    return
if not hc % (qs + 1) == 0:
    print('No')
    return

t = s.split('Q')
pre = len(t[0]) // 2
suf = 0 if len(t) == 1 else len(t[-1]) // 2
a = ['H' * pre] + t[1 : qs] + ['H' * suf]
o = [c for c in 'Q'.join(a)]
g = []
for c in o:
    if c == 'H':
        g += ['H']
    else:
        g += o

print('Yes' if ''.join(g) == s else 'No')