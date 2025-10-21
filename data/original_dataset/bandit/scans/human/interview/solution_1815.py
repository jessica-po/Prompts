counts = {}
rcount = {}

input()

m = 0
for i, x in enumerate(map(int, input().split())):
	if x in counts:
		rcount[counts[x]].remove(x)
		if not rcount[counts[x]]:
			del rcount[counts[x]]
		counts[x] += 1
		if counts[x] not in rcount: rcount[counts[x]] = set()
		rcount[counts[x]].add(x)
	else:
		counts[x] = 1
		if 1 not in rcount: rcount[1] = set()
		rcount[1].add(x)
	keys = list(rcount)
	if len(keys) == 2 and max(keys) - min(keys) == 1 and len(rcount[max(keys)]) == 1 or len(keys) == 2 and min(keys) == 1 and len(rcount[1]) == 1 or len(keys) == 1 and (len(rcount[keys[0]]) == 1 or keys[0] == 1):
		m = max(m, i)

print(m + 1)