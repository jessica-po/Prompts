n = int(input())
s = input()

ans = 0
for i in range(n):
    for j in range(i + 1, n + 1):
        t = s[i:j]
        ans += t.count('U') == t.count('D') and t.count('L') == t.count('R')

print(ans)