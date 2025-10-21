n = sum(list(map(int, input().split())))

A = [0 for i in range(n)]

DP = [[0 for i in range(3)] for i in range(n)]

for i in range(3):
	for j in map(int, input().split()):
		A[j - 1] = i

DP[0] = [A[0] != i for i in range(3)]

for i in range(1, n):
	DP[i][0] = DP[i - 1][0] + (A[i] != 0)
	DP[i][1] = min(DP[i - 1][0], DP[i - 1][1]) + (A[i] != 1)
	DP[i][2] = min(DP[i - 1]) + (A[i] != 2)

print(min(DP[n - 1]))