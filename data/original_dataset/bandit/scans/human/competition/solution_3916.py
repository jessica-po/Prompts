T = 1
for test_no in range(T):
	MAXK = 5000
	n = int(input())
	cnt = [0] * (MAXK + 1)
	primeExponential = [[0 for j in range(MAXK + 1)] for i in range(MAXK + 1)]

	line, num = (input() + ' '), 0
	for c in line:
		if c != ' ': num = num * 10 + (ord(c) - 48)
		else:
			cnt[num] += 1
			num = 0

	for i in range(2, MAXK + 1):
		for j in range(0, MAXK + 1): primeExponential[i][j] += primeExponential[i-1][j]
		tmp, x = i, 2
		while x * x <= tmp:
			while tmp % x == 0:
				primeExponential[i][x] += 1
				tmp //= x
			x += 1
		if tmp > 1: primeExponential[i][tmp] += 1

	bestPD = [1] * (MAXK + 1)
	ans, cur = 0, 0

	for i in range(1, MAXK + 1):
		if cnt[i] == 0: continue
		for j in range(1, MAXK + 1):
			ans += primeExponential[i][j] * cnt[i]
			cur += primeExponential[i][j] * cnt[i]
			if primeExponential[i][j]: bestPD[i] = j

	frequency = [0] * (MAXK + 1)
	while max(bestPD) > 1:
		for i in range(MAXK + 1): frequency[i] = 0
		for i in range(MAXK + 1): frequency[bestPD[i]] += cnt[i]

		bestGroup = max(frequency)
		bestPrime = frequency.index(bestGroup)
		if bestGroup * 2 <= n: break
		if bestPrime == 1: break
		cur -= bestGroup
		cur += (n - bestGroup); ans = min(ans, cur)

		for i in range(MAXK + 1):
			if bestPD[i] != bestPrime: bestPD[i] = 1
			if bestPD[i] == 1: continue
			primeExponential[i][bestPD[i]] -= 1
			while bestPD[i] > 1 and primeExponential[i][bestPD[i]] == 0: bestPD[i] -= 1

	print(ans)