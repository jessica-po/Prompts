a, b = map(int,input().split())
c, d = map(int,input().split())
ONE = set()
TWO = set()
for i in range(b, 50000, a):
    ONE.add(i)
for i in range(d, 50000, c):
    TWO.add(i)

opt = 99999
for i in ONE:
    if i in TWO:
        opt = min(opt, i)
if opt == 99999:
    print(-1)
else:
    print(opt)