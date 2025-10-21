tmp = list(map(int,input().split()))
n,k = tmp[0],tmp[1]
a = list(map(int,input().split()))

cur = a[0]
w = 0
OK = False
for i in range(1,10000):
    op = a[i]
    if cur > op:
        a.append(op)
        w += 1
    else:
        cur = op
        a.append(cur)
        w = 1
    if w >= k:
        OK = True
        break
if OK:
    print(cur)
else:
    print(max(a))