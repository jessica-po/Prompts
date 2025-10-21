import sys
n, l, v1, v2, k = list(map(int, input().split()))
n = (n + k - 1) // k
if n == 1:
	print(l / v2)
	return

L, R = 0, l
for i in range(100):
	M = (L + R) / 2
	S = l - M
	T = M * (n * 2 - 1)- l
	if T * v1 > S * v2:
		R = M
	else:
		L = M

print(M / v2 + S / v1)