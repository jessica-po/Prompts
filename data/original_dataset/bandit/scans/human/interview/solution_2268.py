# import sys
# sys.stdin = open('cf591b.in')

n, m = map(int, input().split())
s = input()

perm = list(range(26))

v = ord('a')

for _ in range(m):
	ss = input()
	i, j = (ord(ss[0]) - v, ord(ss[2]) - v)
	perm[i], perm[j] = perm[j], perm[i]

rev = [perm.index(c) for c in range(26)]
print(''.join(chr(rev[ord(c) - v] + v) for c in s))