n, x = list(map(int, input().split()))
ar = list(map(int, input().split()))

cnt = {}
ans = 0
for val in ar:
	cur = val ^ x
	
	if cur in cnt:
		ans += cnt[cur]
	
	if val in cnt:
		cnt[val] += 1
	else:
		cnt[val] = 1

print(ans)