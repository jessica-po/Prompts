n, c = list(map(int, input().split()))
res1 = [0] * 500001
res = 0
for ai in map(int, input().split()):
	res1[ai] = max(res1[ai], res1[c])
	res1[ai] += 1
	res = max(res, res1[ai] - res1[c])
print(res + res1[c])