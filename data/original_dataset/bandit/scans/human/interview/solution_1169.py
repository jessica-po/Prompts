n, m = map(int, input().split())
if m == 0:
	print(n, n)
	return
if m == n * (n - 1) // 2:
	print(0, 0)
	return
L = 0
R = n + 1
while R - L > 1:
	m1 = (L + R) // 2
	if m1 * (m1 - 1) // 2 < m:
		L = m1
	else:
		R = m1
ans_max = n - R
ans_min = max(0, n - 2 * m)
print(ans_min, ans_max)