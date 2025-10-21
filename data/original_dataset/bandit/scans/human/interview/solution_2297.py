def s(k):
	if k % 2 == 0:
		return k // 2
	else:
		return - (k + 1) // 2


for i in range(int(input())):
	l, r = list(map(int, input().split()))
	print(s(r) - s(l - 1))