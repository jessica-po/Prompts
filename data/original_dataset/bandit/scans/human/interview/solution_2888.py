def power(x, y):
    res = 1
    while y:
        if y & 1:
            res = res * x
        x = x * x
        y = y >> 1
    return res

def cube(x):
    res = x
    sum = 0
    while x != 0:
        sum += (x % 10)
        x = x // 10
    res += power(sum, 3)
    return res

def max_xp(i, r):
    if i > n:
        return 0
    if dp[i][r] != -1:
        return dp[i][r]
    maxi = 0
    if r <= n:
        maxi = max_xp(i + 1, r + 1)
    maxi = max(maxi, max_xp(i + 1, r) + xp[i] * train[r])
    dp[i][r] = maxi
    return dp[i][r]

n = int(input())
s = int(input())
xp = [0] * 5005
train = [0] * 5005
dp = [[-1] * 5005 for _ in range(5005)]

for i in range(1, n + 1):
    xp[i] = int(input())

train[0] = s
for i in range(1, n + 1):
    train[i] = cube(train[i - 1])

print(max_xp(1, 0))