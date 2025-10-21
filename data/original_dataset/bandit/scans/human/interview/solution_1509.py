n = int(input())
v = [0] + [int(e) for e in input().split()]
ans = 0
for a, b in zip(v[:-1], v[1:]):
    if a < b:
        ans += (b-a)*(n-b+1)
    else:
        ans += b*(a-b)
print(ans)