s = input()

ans = 0
for i in range(1, len(s)):
    if int(s[i - 1: i + 1]) % 4 == 0:
        ans += i
for x in s:
    if int(x) % 4 == 0:
        ans += 1

print(ans)