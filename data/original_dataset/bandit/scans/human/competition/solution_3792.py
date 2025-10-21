def ii():
    return int(input())
def mi():
    return list(map(int, input().split()))
def li():
    return list(mi())

# B. The Fair Nut and Strings

n, k = mi()
s = input().strip()
t = input().strip()

ans = 0
jj = 0
for i in range(n):
    if s[i] == t[i]:
        ans += 1
        jj = i + 1
    else:
        break
cur = 2
for j in range(jj, n):
    if s[j] == 'b':
        cur -= 1
    if t[j] == 'a':
        cur -= 1
    if cur >= k:
        ans += k * (n - j)
        break
    ans += cur
    cur *= 2

print(ans)