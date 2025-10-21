N = int(input())
p = input()
M = int(input())
words = [input() for _ in range(M)]
cnt = 0
letters = [set() for _ in range(M)]
used = set()
for c in p:
    used.add(c)
fail = [False]*M

for i, w in enumerate(words):
    for j, c in enumerate(w):
        if p[j] == '*':
            letters[i].add(c)
            if c in used:
                fail[i] = True
        elif p[j] != c:
            fail[i] = True

for i in range(26):
    ch = chr(ord('a') + i)
    ok = True
    for i, s in enumerate(letters):
        ok = ok and (ch in s or fail[i])
    if ok: cnt += 1
print(cnt)