n, m = map(int, input().split())
valists = [10**9 for _ in range(1<<n)]
valists[0] = 0
for i in range(m):
	values, b = map(int, input().split())
	c = list(map(int, input().split()))
	cnt = 0
	for j in range(b):
		cnt += 2**(c[j]-1)
	for j in range(len(valists)):
		x = j|cnt
		valists[x] = min(valists[x], valists[j]+values)
		#print(j, cnt, x, valists)

#print(valists)
ans = valists[2**n-1]
if ans != 10**9:
	print(ans)
else:
	print(-1)