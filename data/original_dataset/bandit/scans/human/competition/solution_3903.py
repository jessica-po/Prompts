#!/usr/bin/env python3
#
# Three States
#
import sys, os
from collections import deque
from pprint import pprint

def read_ints(): return list(map(int, input().split()))
def read_str(): return input().strip()

n, m = read_ints()
s = [read_str() for _ in range(n)]

t = [set(), set(), set()]

for i in range(n):
	for j in range(m):
		if s[i][j] in '123':
			for ii, jj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
				if 0 <= ii < n and 0 <= jj < m:
					if s[ii][jj] in '123.' and s[i][j] != s[ii][jj]:
						t[int(s[i][j]) - 1].add((i, j))
						break

z = [[[1e18] * 3 for j in range(m)] for i in range(n)]
ans = 1e18
for root in range(3):
	q = deque()
	vi = [[False] * m for _ in range(n)]
	for i, j in t[root]:
		q.append((i, j, 0))
		vi[i][j] = True
		z[i][j][root] = 0
	dist = [1e18] * 3
	dist[root] = 0
	while q:
		i, j, d = q.popleft()
		for ii, jj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
			if 0 <= ii < n and 0 <= jj < m and not vi[ii][jj]:
				if s[ii][jj] == '.':
					vi[ii][jj] = True
					q.append((ii, jj, d + 1))
					z[ii][jj][root] = min(z[ii][jj][root], d + 1)
				elif s[ii][jj] != s[i][j] and s[ii][jj] in '123':
					dist[int(s[ii][jj]) - 1] = min(dist[int(s[ii][jj]) - 1], d)
	ans = min(ans, sum(dist))

if ans >= 1e18:
	print(-1)
else:
	for i in range(n):
		for j in range(m):
			if s[i][j] == '.':
				ans = min(ans, sum(z[i][j]) - 2)
	print(ans)