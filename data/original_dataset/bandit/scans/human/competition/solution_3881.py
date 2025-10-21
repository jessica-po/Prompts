n, q = list(map(int, input().split()))
go = dict()
for i in range(q):
    fr, to = input().split()
    go[fr] = to

ans = 0

for i in range(6 ** n):
    cur = i
    s = ''
    for j in range(n):
        s += chr(ord('a') + (cur % 6))
        cur //= 6

    while len(s) > 1:
        fr = s[:2]
        if fr not in go:
            break
        s = go[fr] + s[2:]

    if s == 'a':
        ans += 1

print(ans)