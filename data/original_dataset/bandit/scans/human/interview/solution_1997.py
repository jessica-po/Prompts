import sys
fin = sys.stdin
n = int(fin.readline())
ut = [-1] * n
vc = [[] for i in range(0, n)]
cvc = [[] for i in range(0, n)]
nr = [0] * n
for i in range(0, n - 1):
    a, b = [int(number) for number in fin.readline().split()]
    a -= 1
    b -= 1
    vc[a].append(b)
    cvc[b].append(a)
    nr[a] += 1
size = [0] * n
mx = [0] * n
def nonzero(x):
    if not x:
        return 0
    return 1
stk = []
size = [0] * n
for i in range(0, n):
    if nr[i] == 0:
        stk.append(i)
        size[i] = 1
order = []
while nonzero(stk):
    x = stk.pop(-1)
    order.append(x)
    for p in cvc[x]:
        nr[p] -= 1
        if nr[p] == 0:
            stk.append(p)
h = [0] * n
for i in range(n - 1, -1, -1):
    x = order[i]
    for p in vc[x]:
        h[p] = h[x] + 1
#parcurg
for x in order:
    for p in vc[x]:
        size[x] += size[p]
#maximum
def solv(tp, mx):
    for x in order:
        if h[x] % 2 == tp:
            r = 999999999
            for p in vc[x]:
                r = min(r, size[p] - mx[p] + 1)
            if r == 999999999:
                r = 1
            mx[x] = r
        else:
            r = 0
            for p in vc[x]:
                r += size[p] - mx[p]
            mx[x] = r + 1
solv(0, mx)
print(size[0] - mx[0] + 1, end = ' ')
solv(1, mx)
print(size[0] - mx[0] + 1)