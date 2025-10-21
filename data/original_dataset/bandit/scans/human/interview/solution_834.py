n = int(input())
f = list(map(int, input().split()))
for i in range(n):
    f[i] -= 1

def gcd(a, b):
    while (a != 0 and b != 0):
        a, b = b, a % b
    return a + b

def lcm(a, b):
    return a * b // gcd(a, b)

ans = 1
minn = 0

for i in range(n):
    vis = [False] * n
    cur = i
    st, pr = 0, 0
    while not vis[cur]:
        vis[cur] = True
        cur = f[cur]
        st += 1
    fs = cur
    cur = i
    while cur != fs:
        pr += 1
        cur = f[cur]
    minn = max(minn, pr)
    ans = lcm(ans, st - pr)

print(((max(0, minn - 1))// ans + 1) * ans)