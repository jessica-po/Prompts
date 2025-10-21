n, m = list(map(int, input().split()))
m += 2
l = []
do = False
for i in range(n):
	s = input().strip()
	if s.find('1') != -1 or do:
		do = True
		l.append(s)
n = len(l)
if n == 0:
	print(0)
	return


dp = []
for i in range(n):
	dp.append([None] * 2)

for i in range(n):
	R = 0
	for j in range(m):
		if l[i][j] == '1':
			R = j
	L = m - 1
	for j in range(m - 1, -1, -1):
		if l[i][j] == '1':
			L = j
	if i == 0:
		dp[0][0] = R
		dp[0][1] = (m - 1 - L)
	else:
		dp[i][0] = min(dp[i - 1][0] + 2 * R, dp[i - 1][1] + (m - 1)) + 1
		dp[i][1] = min(dp[i - 1][0] + (m - 1), dp[i - 1][1] + 2 * (m - 1 - L)) + 1
# print(dp)
print(dp[-1][0])