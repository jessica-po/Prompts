n, k, m = map(int, input().split())
a = list(map(int, input().split()))

all = [0] * m
for x in a:
	all[x % m] += 1

was = 0
for i in range(m):
	if(all[i] >= k and was == 0):
		print("Yes")
		for x in a:
			if(x % m == i and was < k):
				print(x, end = ' ')
				was += 1

if (was != k):
	print("No")