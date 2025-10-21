n, k = map(int, input().split())
s = input()
our = set()
opened = set()
for i in range(ord('A'), ord('Z') + 1):
    sym = chr(i)
    if sym in s:
        our.add(s.rfind(sym))
for i in range(len(s)):
    if s[i] not in opened:
        opened.add(s[i])
        k -= 1
        if k < 0:
            print('YES')
            return
    if i in our:
        k += 1
print('NO')