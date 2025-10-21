n = int(input())
a = input().replace(' ', '')
ans = 0
for i in range(n):
    for j in range(i, n):
        s = a[i:j + 1]
        ans = max(ans, s.count('0') + (a[:i] + a[j + 1:]).count('1'))
print(ans)