import sys
def input():
	return sys.stdin.readline()[:-1]
from bisect import bisect

def ctoi(c):
	return ord(c) - ord("a")
	print(ans)

T = int(input())
for _ in range(T):
	s = input()
	t = input()
	if not (set(s) >= set(t)):
		print(-1)
	else:
		alph = [[] for _ in range(26)]
		for i in range(len(s)):
			alph[ctoi(s[i])].append(i)
		for a in alph:
			if a:
				a.append(a[0] + len(s))
		#print(alph)
		cur = len(s)-1
		ans = 0
		for i in range(len(t)):
			ind = bisect(alph[ctoi(t[i])], cur)
			ans += alph[ctoi(t[i])][ind] - cur
			cur = alph[ctoi(t[i])][ind] % len(s)
		print(-(-ans//len(s)))