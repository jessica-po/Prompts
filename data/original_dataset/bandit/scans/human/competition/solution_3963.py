p = 1000000007

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())

d = [1] * 300001
td = [0] * 300001
L = b[0]
for i in range(1, n):
	if a[i - 1] != 1:
		t = m % a[i - 1]
		if L < t:
			print(0)
			return
		m //= a[i - 1]
		for j in range((L - t) // a[i - 1] + 1):
			d[j] = d[t]
			t += a[i - 1]
		L = j
	k = 0
	for j in range(L + b[i] + 1):
		if j <= L:
			k += d[j]
		k %= p
		td[j] = k
		if j >= b[i]:
			k -= d[j - b[i]]
	L += b[i]
	for j in range(L + 1):
		d[j] = td[j]
print(d[m] if m <= L else 0)