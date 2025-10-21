def ii():
    return int(input())
def mi():
    return list(map(int, input().split()))
def li():
    return list(mi())
MX = 10 ** 5

n = ii()
fac = 2
pr = []
while fac * fac <= n:
    c = 0
    while n % fac == 0:
        c += 1
        n //= fac
    if c:
        pr.append((fac, c))
    fac += 1
if n > 1:
    pr.append((n, 1))
if pr:
    mx = max(e for p, e in pr)
    mn = min(e for p, e in pr)
    mx2 = 1
    cnt = 0
    while mx2 < mx:
        mx2 *= 2
        cnt += 1
    ans = cnt + int(mn != mx2)
    pdt = 1
    for p, e in pr:
        pdt *= p
else:
    pdt, ans = 1, 0
print(pdt, ans)