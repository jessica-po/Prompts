input()
res_h = 0
res_ha = 0
res_har = 0
res_hard = 0
for s, a in zip(input(), list(map(int, input().split()))):
	if s == 'h':
		res_h += a
	elif s == 'a':
		res_ha = min(res_ha + a, res_h)
	elif s == 'r':
		res_har = min(res_har + a, res_ha)
	elif s == 'd':
		res_hard = min(res_hard + a, res_har)
print(res_hard)