res = 1
started = False
seen = set()
codes = set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
for ch in input():
	if ch == '?':
		if started:
			res *= 10
		else:
			res *= 9
	elif (ch in codes) and (ch not in seen):
		if not started:
			res *= len(codes) - len(seen) - 1
		else:
			res *= len(codes) - len(seen)
		seen.add(ch)
	started = True
print(res)