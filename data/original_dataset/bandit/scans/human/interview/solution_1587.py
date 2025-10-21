n = int(input())
c = input()

w = 0
r = c.count('R')
i = 0
ans = max(w, r)
while i <= n - 1:
    if c[i] == 'W':
        w += 1
    else:
        r -= 1
    ans = min(ans, max(w, r))
    i += 1
print(ans)