N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = []
c = 2**30
r = 2**30
while r:
    r //= 2
    l = sum(-(-a//c)-1 for a in A)
    if l > K:
        c += r
    else:
        ans.append(c)
        c -= r

print(ans and min(ans) or 1)