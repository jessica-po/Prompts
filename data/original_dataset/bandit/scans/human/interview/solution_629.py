n = int(input())
a = [[], []]
a[0] = list(map(int, input().split()))
a[1] = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = float('+inf')
for i in range(n):
	for j in range(n):
		if i == j:
			continue
		cur = sum(a[1][i:]) + sum(a[0][:i]) + sum(a[0][:j]) +  sum(a[1][j:]) + b[i] + b[j]
		ans = min(ans, cur)
print(ans)