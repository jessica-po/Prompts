n = int(input())
s = ''
s1 = ''
ans = 0
for i in range(n):
    s = input()
    if (s != s1):
        ans += 1
    s1 = s
print(ans)