from collections import Counter

s = input()
n = int(input())

d = Counter()

for c in s:
    d[c] += 1

if len(d) > n:
    print(-1)
else:
    left = 0
    right = 10**10
    s = ""
    lastok = ("", 0)
    while left + 1 < right:
        mid = (left + right) // 2
        s = ""
        for (c, cnt) in list(d.items()):
            cntnow = (cnt - 1) // mid + 1
            s += c * cntnow
        if len(s) < n:
            s += 'a' * (n - len(s))
        if len(s) == n:
            lastok = (s, mid)
            right = mid
        else:
            left = mid
    print(lastok[1])
    print(lastok[0])