n = int(input())
s = list(input())
sit = 0
for i in range(n):
    if s[i] == 'x':
        sit += 1
ans = 0
i = 0
while i < n and sit < n - sit:
    if s[i] == 'X':
        sit += 1
        ans += 1
        s[i] = 'x'
    i += 1
i = 0
while i < n and sit > n - sit:
    if s[i] == 'x':
        sit -= 1
        ans += 1
        s[i] = 'X'
    i += 1
print(ans)
print(''.join(s))