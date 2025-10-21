n, m = list(map(int, input().split()))
v = list(map(int, input().split()))
v = sorted(v)

diff = 10**10
for i in range(0, len(v)):
    if i+n-1 < len(v): diff = min(diff, v[i+n-1] - v[i])

print(diff)