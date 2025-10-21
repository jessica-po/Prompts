n = int(input())
parent = [-1]*n
isresp = [1]*n
for i in range(n):
	p, r = list(map(int, input().split()))
	p -= 1
	if r == 0:
		isresp[i] = 0
		if p>=0:
			isresp[p] = 0
nore = []
for i in range(n):
	if isresp[i] == 1:
		nore.append(i+1)
if not nore:
	print(-1)
else:
	print(" ".join(map(str, nore)))