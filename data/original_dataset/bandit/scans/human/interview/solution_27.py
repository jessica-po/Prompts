n = int(input())
st = input()
ans = n
now = ''
ma = 0
for i in range(n // 2):
    now += st[i]
    t = ''
    for j in range(i + 1, 2 * i + 2):
        t += st[j]
    if t == now:
        ma = i
print(ans - ma)