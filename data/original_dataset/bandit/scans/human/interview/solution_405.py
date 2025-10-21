n = int(input())
s = input()
l = 0
ans = 0
while l < len(s) and s[l] == '<':
    ans += 1
    l += 1

r = n - 1
while r >= 0 and s[r] == '>':
    ans += 1
    r -= 1

print(ans)