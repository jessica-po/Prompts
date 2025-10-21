q = int(input())
for query in range(q):
	k, n, a, b = list(map(int,input().split()))
	if n * b > k:  
		print(-1)
	else:
		print(min(n, (k-n*b-1)//(a-b)))