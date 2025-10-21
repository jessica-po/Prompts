import sys

NORM = 2000000
LIMIT = NORM * 2 + 1

class segmentTree:
	def __init__(self, n):
		self.n = n
		self.t = [0] * (n * 2)
		self.lazy = [0] * n

	def apply(self, p, value):
		self.t[p] += value
		if p < self.n:
			self.lazy[p] += value
		
	def build(self, p):
		while p > 1:
			p >>= 1
			self.t[p] = max(self.t[p * 2], self.t[p * 2 + 1]) + self.lazy[p]
	
	def push(self, p):
		log = 0
		while (1 << log) <= self.n:
			log += 1
		
		for s in range(log, 0, -1):
			parent = p >> s
			if self.lazy[parent] != 0:
				self.apply(parent * 2, self.lazy[parent])
				self.apply(parent * 2 + 1, self.lazy[parent])
				self.lazy[parent] = 0 
	
	def inc(self, l, r, value):
		l += self.n
		r += self.n
		l0, r0 = l, r
		while l < r:
			if l & 1: 
				self.apply(l, value)
				l += 1
			if r & 1:
				self.apply(r - 1, value)
				r -= 1
			l >>= 1
			r >>= 1
		self.build(l0)
		self.build(r0 - 1)
	
	def query(self, l, r):
		l += self.n
		r += self.n
		self.push(l)
		self.push(r - 1)
		res = 0
		while l < r:
			if l & 1:
				res = max(res, self.t[l])
				l += 1
			if r & 1:
				res = max(res, self.t[r - 1])
				r -= 1
			l >>= 1
			r >>= 1
		return res

inp = [int(x) for x in sys.stdin.read().split()]
n, r = inp[0], inp[1]
inp_idx = 2

points = []
env = {}

for _ in range(n):
	x, y = inp[inp_idx], inp[inp_idx + 1]
	inp_idx += 2

	new_x = x - y
	new_y = x + y
	new_x += NORM
	new_y += NORM
	
	if not new_y in env:
		env[new_y] = []
	env[new_y].append(new_x)
	points.append([new_x, new_y])

sq_side = r * 2

tree = segmentTree(LIMIT)

ys = []
for y in list(env.keys()):
	ys.append(y)
ys = sorted(ys)

ans = 0
last = 0
for i in range(len(ys)):
	y = ys[i]
	while i > last and ys[last] < y - sq_side:
		low_y = ys[last]
		for x in env[low_y]:
			low_x = max(0, x - sq_side)
			tree.inc(low_x, x + 1, -1)
		last += 1
	
	for x in env[y]:
		low_x = max(0, x - sq_side)
		tree.inc(low_x, x + 1, +1)

	ans = max(ans, tree.query(0, LIMIT))

print(ans)