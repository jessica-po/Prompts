def count(p, s):
    start = 0
    c = 0
    while True:
        try:
            pos = s.index(p, start)
            c += 1
            start = pos + 1
        except ValueError:
            return c

s = input()
n = int(input())

pravs = []
for i in range(n):
    p, l, r = input().split()
    l = int(l); r = int(r)
    pravs.append((p, l, r))

var = set()
for l in range(len(s)):
    for r in range(l+1, len(s)+1):
        pods = s[l:r]
        for prav in pravs:
            if not prav[1] <= count(pods, prav[0]) <= prav[2]:
                break
        else:
            var.add(pods)

print(len(var))