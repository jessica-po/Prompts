def ii():
    return int(input())
def mi():
    return map(int, input().split())
def li():
    return list(mi())

n, M = mi()
a = [0] + li() + [M]
n = len(a)
ans = 0
p = [0] * n
q = [0] * n
for i in range(1, n):
    p[i] = p[i - 1]
    q[i] = q[i - 1]
    if i % 2 == 0:
        p[i] += a[i] - a[i - 1]
    else:
        q[i] += a[i] - a[i - 1]

ans = q[-1]
for i in range(1, n):
    if a[i] == a[i - 1] + 1:
        continue
    if i % 2 == 0:
        ans = max(ans, q[i] + 1 + p[-1] - p[i], q[i] + a[i] - a[i - 1] - 1 + p[-1] - p[i])
    else:
        ans = max(ans, q[i] - 1 + p[-1] - p[i], q[i] - (a[i] - a[i - 1] - 1) + p[-1] - p[i])
print(ans)