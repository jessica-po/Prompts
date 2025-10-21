n, m = (int(x) for x in input().split())
winners = [0] * n
for i in range(m):
	a = [int(x) for x in input().split()]
	winners[a.index(max(a))] += 1
print(winners.index(max(winners)) + 1)