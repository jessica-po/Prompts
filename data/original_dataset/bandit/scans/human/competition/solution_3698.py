mas = [[] for i in range(1001)]
mas[0].append(1)
mas[0].append(1)
for i in range(1, 1000):
    mas[i].append(1)
    for j in range(1, i):
        mas[i].append((mas[i - 1][j] + mas[i - 1][j - 1]) % (10 ** 9 + 7))
    mas[i].append(1)


def c(k, n):
    if k > n:
        return 0
    if k < 0:
        return 0
    nonlocal mas
    return mas[n][k]


m = [0] * 1000
for i in range(1, 1000):
    nw = i
    t = 0
    while nw != 1:
        nw = sum([int(j) for j in str(bin(nw)[2:])])
        t += 1
    m[i] = t
m[1] = 0
n = input()
k = int(input())
if k >= 6:
    print(0)
    return
if k == 0:
    print(1)
    return
if k == 1:
    print(len(n) - 1)
    return
ans = 0
for kkk in range(1, 1000):
    if m[kkk] == k - 1:
        nw = kkk
        t = 0
        for i in range(len(n)):
            if n[i] == '1':
                ans += c(nw - t, len(n) - 1 - i)
                ans %= 10 ** 9 + 7
                t += 1
        if sum([int(j) for j in n]) == kkk:
            ans += 1
            ans %= 10 ** 9 + 7


print(ans)