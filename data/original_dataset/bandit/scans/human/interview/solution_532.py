now = "a"
ans = 0
S = input()
for s in S:
    x = abs(ord(s) - ord(now))
    ans += min(x, 26 - x)
    now = s
print(ans)