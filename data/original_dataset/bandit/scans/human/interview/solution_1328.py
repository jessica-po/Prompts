def main():
	n, ma, mb, *L = list(map(int, open(0).read().split()))
	M = 1 << 30
	dp = [[M] * 420 for _ in range(420)]
	dp[0][0] = 0
	ua = ub = 15
	for a, b, c in zip(*[iter(L)] * 3):
		for i in range(ua, -1, -1):
			for j in range(ub, -1, -1):
				t = dp[i][j] + c
				if dp[i + a][j + b] > t:
					dp[i + a][j + b] = t
					if ua < i + a:
						ua = i + a
					if ub < j + b:
						ub = j + b
	ans = M
	_ma, _mb = ma, mb
	while _ma < 410 > _mb:
		ans = min(ans, dp[_ma][_mb])
		_ma += ma
		_mb += mb
	print((ans if ans < M else -1))


def __starting_point():
	main()

__starting_point()