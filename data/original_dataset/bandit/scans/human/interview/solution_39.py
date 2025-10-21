s = input()
mx = 0
n = len(s)
for l in range(n):
    for r in range(l, n):
        if s[l:r+1] != s[l:r+1][::-1]:
            mx = max(mx, r - l + 1)
print(mx)